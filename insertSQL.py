import sqlite3

conn = sqlite3.connect('Student.db')
print("Opened database successfully")

conn.execute("INSERT INTO STUDENT (NAME,ROLLNO,EMAIL) \
      VALUES ('Joel', 1, 'joel@gmail.com')")

conn.commit()
print("Records created successfully")
conn.close()