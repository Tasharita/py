import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (21, 'MARK',23,90200.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (22, 'JOY',24,89000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (23, 'MARTHA',31,34200.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (24, 'JOB',51,56200.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (25, 'ANGEL',36,34200.00)")



conn.commit()
print("Records inserted successfully")
conn.close()