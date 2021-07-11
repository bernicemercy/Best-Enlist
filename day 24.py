import json
import sqlite3

jfile = [
{'Name ': 'Bernice','Age':21,'Salary' : 3000000.00,'Permenant': True},
{'Name' : 'Beryl','Age':23,'Salary':3000000.00,'Permenant':True},
{'Name' : 'Alex','Age': 18,'Salary':3000000.00,'Permenant ':True},
{'Name' : 'Isabel' ,'Age':17,'Salary':3000000.00,'Permenant' :True}
    ]
data = json.dumps(jfile)
print(data)

connection = sqlite3.connect('mudb.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS employees(Name,Age,Salary,Permenant)")

data_in = "INSERT INTO employees (Name,Age,Salary,Permenant)VALUES(%s)"
for i in range(len(data)):
    employees[i] = data[i]
