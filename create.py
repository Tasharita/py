import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEES(
ID INT PRIMARY KEY NOT NULL ,
NAME STRING NOT NULL ,
AGE INT NOT NULL,
SALARY REAL NOT NULL);
''')
print("Table created successfully")
conn.close()