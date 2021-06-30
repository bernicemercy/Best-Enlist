#1.
import sqlite3
print("Connecting to database")
connection = sqlite3.connect("best_enlist.db")
print("Database created successfully")
cursor = connection.cursor()
command = """ CREATE TABLE IF NOT EXISTS
doctors_patients(Doctor_id INTERGER PRIMARY KEY,Doctor_name TEXT NOT NULL,Patients_visited INTEGER)"""
cursor.execute(command)

cursor.execute("INSERT INTO Doctors_patients VALUES(1234,'Beryl',12)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1235,'Princess',19)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1236,'Bernice',0)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1237,'Mercy',0)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1238,'Sharon',0)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1239,'Paul',4)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1230,'Alex',1)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1231,'Isabel',2)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1232,'Katielyn',0)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1233,'Caroline',17)")
cursor.execute("INSERT INTO Doctors_patients VALUES(1221,'Klaus Mickaelson',23)")
#2
cursor.execute("SELECT Doctor_name from doctors_patients WHERE Patients_visited>5")
r = cursor.fetchall()
print("Doctors with more than 5 patients")
for x in r:
    print(x)
#3
cursor.execute("SELECT Doctor_name from doctors_patients WHERE Patients_visited=0")
results = cursor.fetchall()
print("Doctors with more 0 patients")
for x in results:
    print(x)
print("Connection closing....")
connection.close()
print("Connection closed")
