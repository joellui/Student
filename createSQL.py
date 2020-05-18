import sqlite3

conn = sqlite3.connect('Student.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE STUDENT
         (NAME           TEXT    NOT NULL,
         ROLLNO INT PRIMARY KEY    NOT NULL,
         EMAIL         TEXT     NOT NULL);''')
print("Table created successfully")

conn.close()