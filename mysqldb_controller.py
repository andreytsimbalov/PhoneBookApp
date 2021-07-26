# database-class connect to mysql database

import mysql.connector as mysql_conn
import json

class database():
    def __init__(self):
        self.setUserId()
        with open('data/mysql_log_pas.json', 'r', encoding='utf-8') as f:
            self.sql_data = json.load(f)
        try:
            self.connection = mysql_conn.connect(
                user=self.sql_data['user'],
                password=self.sql_data['password'],
                host=self.sql_data['host'],
                port=self.sql_data['port'],
                database=self.sql_data['database']
            )
            self.cur = self.connection.cursor(buffered=True)
            print("Success connection to DB")
        except mysql_conn.Error as e:
            print(f"Error connecting to DB: {e}")

    def takeSelectCommand(self, str = "", table_id = 0):
        if str == "":
            table_dict = {
                0: 'users',
                1: 'phone_contacts',
            }
            str = "SELECT * FROM "+table_dict[table_id]
        self.cur.execute(str)
        res = []
        for c in self.cur:
            res.append(c)
        return res

    def printSelectCommand(self, str = "", table_id = 0):
        res = self.takeSelectCommand(str,table_id)
        for r in res:
            print(r)

    def addDataInUser(self, login, password, date_of_birth):
        self.cur.execute("SELECT * FROM users WHERE (login, password) = (%s,%s)",
                    (login, password))
        if self.cur.fetchone() != None:
            return 1
        try:
            statement = "INSERT INTO users (login, password, date_of_birth) VALUES (%s, %s, %s)"
            data = (login, password, date_of_birth)
            self.cur.execute(statement, data)
            self.connection.commit()
            print("Successfully added entry to database in users")
        except mysql_conn.Error as e:
            print(f"Error adding entry to database: {e}")
        return 0

    def addDataInPhoneContacts(self, user_id, name, phone_number, date_of_birth):
        self.cur.execute("SELECT * FROM phone_contacts WHERE (user_id, name, phone_number, date_of_birth) = (%s, %s,%s,%s)",
                    (user_id, name, phone_number, date_of_birth))
        if self.cur.fetchone() != None:
            return 1
        try:
            statement = "INSERT INTO phone_contacts (user_id, name, phone_number, date_of_birth) VALUES (%s, %s, %s, %s)"
            data = (user_id, name, phone_number, date_of_birth)
            self.cur.execute(statement, data)
            self.connection.commit()
            print("Successfully added entry to database in phone_contacts")
        except mysql_conn.Error as e:
            print(f"Error adding entry to database: {e}")
        return 0

    def setUserId(self, id = -1):
        self.id = id

    def selectAlphabeticPart(self, str):
        statement = "SELECT * FROM phone_contacts where (LEFT(name,1) > %s AND LEFT(name,1) < %s) AND (user_id = %s)"
        data = (str[0], str[-1], self.id)
        self.cur.execute(statement, data)
        res = []
        for c in self.cur:
            res.append(c)
        return res

if __name__ == "__main__":
    db = database()

    print("users")
    db.printSelectCommand(table_id=0)
    print()
    print("phone_contacts")
    db.printSelectCommand(table_id=1)
    print()
