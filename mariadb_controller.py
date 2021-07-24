import mysql.connector as mariadb
import datetime


class database():
    def __init__(self):
        self.setUserId()
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
        except mariadb.Error as e:
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
        except mariadb.Error as e:
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

    users = db.printSelectCommand(table_id=0)


    # db.cur.execute("ALTER TABLE users    DROP    COLUMN    remember_me")
    # db.connection.commit()

    # db.cur.execute("delete from users")
    # db.connection.commit()


    # # db.cur.execute("SELECT LEFT(name,1) FROM phone_contacts")
    # statement = "SELECT * FROM phone_contacts where (LEFT(name,1) > %s AND LEFT(name,1) < %s) AND (user_id = %s)"
    # data = ('k', 'z', 1)
    # db.cur.execute(statement, data)
    #
    # # db.cur.execute("SELECT * FROM phone_contacts where (LEFT(name,1) > 'k' AND LEFT(name,1) < 'z') AND (id = 2)",)
    # cur_res = db.cur
    # for i in cur_res:
    #     print(i)

    # db.setUserId(1)
    # res = db.selectAlphabeticPart('ая')
    # print(res)
    # print(db.id)
    #
    # db.printSelectCommand(table_id=1)


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
