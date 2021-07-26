# creates a database on a new device
# the device must have a mysql server

import mysql.connector as mysql_conn
import json

if __name__ == "__main__":
    with open('data/mysql_log_pas.json', 'r', encoding='utf-8') as f:
        sql_data = json.load(f)

    connection = mysql_conn.connect(
        user=sql_data['user'],
        password=sql_data['password'],
        host=sql_data['host'],
        port=sql_data['port']
    )
    cur = connection.cursor(buffered=True)
    print("Success connection to DB")

    try:
        cur.execute("CREATE DATABASE " + sql_data['database'])
        print("Database", sql_data['database'], "created")
        connection.commit()
    except:
        print("Database", sql_data['database'], "was created earlier")
    connection.close()

    connection = mysql_conn.connect(
        user=sql_data['user'],
        password=sql_data['password'],
        host=sql_data['host'],
        port=sql_data['port'],
        database=sql_data['database']
    )
    cur = connection.cursor(buffered=True)

    try:
        # create phone_contacts
        command = "CREATE TABLE `phone_contacts` (" \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "`user_id` int NOT NULL," \
                  "`name` varchar(100) DEFAULT NULL," \
                  "`phone_number` varchar(100) DEFAULT NULL," \
                  "`date_of_birth` date DEFAULT NULL," \
                  "PRIMARY KEY (`id`)," \
                  "KEY `phone_contacts_FK` (`user_id`)," \
                  "CONSTRAINT `phone_contacts_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)" \
                  ")"

        cur.execute(command)
        connection.commit()
    except:
        print("Table phone_contacts was created earlier")

    try:
        # create users
        command = "CREATE TABLE `users` (" \
                  "`login` varchar(32) NOT NULL," \
                  "`password` varchar(32) NOT NULL," \
                  "`date_of_birth` date NOT NULL," \
                  "`id` int NOT NULL AUTO_INCREMENT," \
                  "PRIMARY KEY (`id`)" \
                  ")"
        cur.execute(command)
        connection.commit()
    except:
        print("Table users was created earlier")

    cur.execute("SHOW TABLES")

    print("Tables:", cur.fetchall())
