#read a jpeg image and print the image file
from PIL import Image
img = open('C:/Users/hp/Pictures/iuddd.jpg')
img.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#merge two pdf files using python script
import PyPDF2
pdf1 = open('sdddd.pdf','rb')
pdf2 = open('cryptography_with_python_tutorial.pdf','rb')

pdf1reader = PyPDF2.PdfFileReader(pdf1)
pdf2reader = PyPDF2.PdfFileReader(pdf2)

pdfwriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1reader.numPages):
    pageobj = pdf1reader.getPage(pageNum)
    pdfwriter.addPage(pageobj)

for pageNum in range(pdf2reader.numPages):
    pageobj = pdf2reader.getPage(pageNum)
    pdfwriter.addPage(pageobj)

pdfoutputfile = open('skk.pdf','wb')
pdfwriter.write(pdfoutputfile)

pdfoutputfile.close()
pdf1.close()
pdf2.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#scrap a website and store the data into db

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8421436728'
)
dbse=mydb.cursor()
dbse.execute('DROP DATABASE IF EXISTS webdata1')
dbse.execute('CREATE DATABASE webdata1')
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8421436728',
    database='webdata1'
)
dbse = mydb.cursor()
dbse.execute('DROP TABLE IF EXISTS webscraping1')
dbse.execute("CREATE TABLE webscraping1 (address VARCHAR(255))")
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
count = 1
tre =[]
tr=[]
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#write queries to filter the data in db

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    password="8421436728"
)
dbse = mydb.cursor()

dbse.execute('SHOW DATABASES')

#for entry in dbse:
#   print(entry)

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="8421436728",
    database="DOCTOR_1"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM doctors WHERE patient_visited = 0")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)