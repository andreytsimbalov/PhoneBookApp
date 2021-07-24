import mysql.connector as mariadb
import datetime


class database():
    def __init__(self):
        try:
            self.connection = mariadb.connect(
                user='root',
                password='admin123',
                host='localhost',
                port='3306',
                database="phonebook"
            )
            self.cur = self.connection.cursor(buffered=True)
            print("Success connection to DB")
        except mariadb.Error as e:
            print(f"Error connecting to DB: {e}")


    def addDataInUser(self, login, password, date_of_birth, remember_me=0):
        self.cur.execute("SELECT * FROM users WHERE (login, password, date_of_birth) = (%s,%s,%s)",
                    (login, password, date_of_birth))
        if self.cur.fetchone() != None:
            return 1

        try:
            statement = "INSERT INTO users (login, password, date_of_birth, remember_me) VALUES (%s, %s, %s, %s)"
            data = (login, password, date_of_birth, remember_me)
            self.cur.execute(statement, data)
            self.connection.commit()
            print("Successfully added entry to database in users")
        except mariadb.Error as e:
            print(f"Error adding entry to database: {e}")

        return 0

    def addDataInPhoneContacts(self, user_id, name, phone_number, date_of_birth):
        self.cur.execute("SELECT * FROM phone_contacts WHERE (name, phone_number, date_of_birth) = (%s,%s,%s)",
                    (name, phone_number, date_of_birth))
        if self.cur.fetchone() != None:
            return 1

        try:
            statement = "INSERT INTO phone_contacts (user_id, name, phone_number, date_of_birth) VALUES (%s, %s, %s, %s)"
            data = (user_id, name, phone_number, date_of_birth)
            self.cur.execute(statement, data)
            self.connection.commit()
            print("Successfully added entry to database in phone_contacts")
        except mariadb.Error as e:
            print(f"Error adding entry to database: {e}")

        return 0

#
# # cur.execute("SELECT * FROM users WHERE id=2")
# 
# qwe = 'name123w2'
# asd = 'number333'
# user_id = 4
# 
# now = datetime.datetime.now()
# formatted_date = now.strftime('%Y-%m-%d')
# res = addDataInPhoneContacts(user_id,qwe,asd,formatted_date)
# print("Result of adding tuple in users:", res)
# 
# 
# # cur.execute("SELECT * FROM users WHERE date_of_birth = %s" % (datetime.datetime(2001, 12, 20)))  # AND password = %s
# cur.execute("SELECT * FROM phone_contacts")
# 
# for i in cur:
#     print(i)
# 
# # result=cur.fetchone()
# # print(result)
# # print(result == None)
# 
# 
# cur.execute("SELECT * FROM users WHERE id=1")
# 
# 
# # mariadb_connection.commit()
# connection.close()