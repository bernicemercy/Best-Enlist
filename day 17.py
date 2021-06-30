#1
import sqlite3
#creating the database
print("Connecting to database")
connection = sqlite3.connect("best_enlist.db")
print("Database created successfully")
cursor = connection.cursor()
print("The version of sqlite3 used is : ",sqlite3.sqlite_version)
#2
table1 = """ CREATE TABLE IF NOT EXISTS
employee(employee_id INTEGER PRIMARY KEY,employee_name TEXT)"""
cursor.execute(table1)
cursor.execute("INSERT INTO employee VALUES(1234,'Bernice')")
cursor.execute("INSERT INTO employee VALUES(1235,'Mercy')")
cursor.execute("INSERT INTO employee VALUES(1236,'Sharon')")

cursor.execute("SELECT * FROM employee")

#3
cursor.execute("SELECT employee_name FROM employee")


results = cursor.fetchall()
print(results)
print("Closing connections...")
connection.close()
print("Connection closed")
