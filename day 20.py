import sqlite3
connection = sqlite3.connect('employees.db')
cursor = connection.cursor()
table1 = """CREATE TABLE IF NOT EXISTS
employee(employee_id INTEGER PRIMARY KEY,employee_name TEXT, salary FLOAT)"""
cursor.execute(table1)
cursor.execute("INSERT INTO employee VALUES(1234,'Bernice',50000.00)")
cursor.execute("INSERT INTO employee VALUES(1235,'Mercy',650000.0)")
cursor.execute("INSERT INTO employee VALUES(1236,'Sharon',100000.0)")

cursor.execute("SELECT * FROM employee")
result = cursor.fetchall()
print(result)
#1
cursor.execute("SELECT MIN(salary) as minimum FROM employee")
mini = cursor.fetchall()
print(mini)
cursor.execute("SELECT MAX(salary) as minimum FROM employee")
maxi = cursor.fetchall()
print(maxi)
#2
cursor.execute("SELECT count(salary) as c FROM employee")
c = cursor.fetchall()
print(c)
#3
cursor.execute("SELECT SUBSTRING(employee_name,0,2) FROM employee as EXTRACTSTRING")
m = cursor.fetchall()
print(m)
