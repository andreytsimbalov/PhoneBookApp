
import mariadb
import sys

# Connect to MariaDB Platform
conn = mariadb.connect(
    user="root",
    password="admin123",
    host="localhost",
    port=3306,
    database="phonebook"
)

# Get Cursor
cur = conn.cursor()