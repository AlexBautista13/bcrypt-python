import sqlite3
conn = sqlite3.connect('demo.db')


print("Database connection successful.")

conn.execute('''CREATE TABLE EMPLOYEES 
                (ID INTERGER PRIMARY KEY NOT NULL,
                USERNAME TEXT NOT NULL,
                PASSWORD TEXT NOT NULL,
                AGE INT NOT NULL); ''')

print("TABLE created successfully")

conn.close()