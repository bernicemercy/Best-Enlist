from PIL import Image

img = Image.open(r"C:\Users\Bernice\Desktop\bernice\maple.jpg")
print(img.format)
img.show()

import PyPDF2 
 
# Open the files that have to be merged one by one
pdf1File = open(r'C:\Users\Bernice\Desktop\bernice\gate AdmitCard.pdf', 'rb')
pdf2File = open(r'C:\Users\Bernice\Desktop\bernice\gate syllabus.pdf', 'rb')
 
# Read the files that you have opened
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
 
# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()
 
# Loop through all the pagenumbers for the first document
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 
# Loop through all the pagenumbers for the second document
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
 
# Close all the files - Created as well as opened
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#4. Write queries to filter the data in db
import sqlite3
mydb = sqlite3.connect("best_enlist.db")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee WHERE employee_name='Bernice' ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
#Output
#('John', 'Highway 21')
