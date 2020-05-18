import sqlite3
conn = sqlite3.connect('Student.db')
print("Opened database successfully")

cursor = conn.execute("SELECT name, rollno, email from STUDENT")
for row in cursor:
    print("NAME = ", row[0])
    print("ROLL_NO = ", row[1])
    print("EMAIL = ", row[2], "\n")

print("Operation done successfully")
conn.close()