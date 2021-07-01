# Day 19
# Create an Excel with data of Student database and add all the values which is required for student management database, Read the excel file and add the datas into a DB 
import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sudharsan98",
  database = "best-enlist"
)

cur = db.cursor()
cur.execute("CREATE TABLE students(Roll_no int, Name VARCHAR(255), Department VARCHAR(255), CGPA float)")
db.close()


import mysql.connector
import xlrd
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sudharsan98",
  database = "best-enlist"
)

cur = db.cursor()
loc=('C:\\Users\\User\\Desktop\\New folder\\Welocme1.xlsx')
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range (1,5):
    print(tuple(sheet.row_values(i)))

sql="INSERT into students (Roll_no,Name,Department,CGPA) values(%s,%s,%s,%s)"
val=("207","Zoro","Mech","7.1")
cur.execute(sql,val)

db.commit()
cur.execute("SELECT * FROM students")

myresult = cur.fetchall()

for x in myresult:
  print(x)

#Output:-
#(201.0, 'Kakashi', 'ECE', 8.0)
#(202.0, 'Luffy', 'EEE', 7.4)
#(208.0, 'Gojo', 'IT', 6.9)
#(256.0, 'Levi', 'CSC', 8.7)
#(207, 'Zoro', 'Mech', 7.1)



