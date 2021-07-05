#create db with doctors and doctor id & patient visited
import mysql.connector
mydb1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8421436728",
)
dbse = mydb1.cursor()
dbse.execute('DROP DATABASE IF EXISTS DOCTOR_1')
dbse.execute('CREATE DATABASE DOCTOR_1')
dbse.execute("SHOW DATABASES")
myresult = dbse.fetchone()
for entry in myresult:
   print("Database:",entry)

mydb1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8421436728",
    database="DOCTOR_1"
)
dbse = mydb1.cursor()

dbse.execute("CREATE TABLE doctors(dr_id VARCHAR(255),patient_visited VARCHAR(255))")
sql1 = "INSERT INTO doctors(dr_id,patient_visited) VALUES (%s ,%s)"
val1 = [
    ('dr_1','15'),
    ('dr_2','12'),
    ("dr_3",'13'),
    ('dr_4','45'),
    ('dr_5','05'),
    ("dr_6",'00'),
    ('dr_7','23')
]
dbse.executemany(sql1,val1)
mydb1.commit()
print(dbse.rowcount, "Doctor data is inserted ")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#get the doctors who have more than 5 patient visited
dbse1 = mydb1.cursor()
dbse1.execute('SELECT * FROM doctors WHERE patient_visited>5')
myresult1 = dbse1.fetchall()
print("doctors with more than 5 patient visited are :")
for z in myresult1:
    print(z)
#----------------------------------------------------------------------------------------------------------------------------------------------------------


#get the doctor with no patient visited
dbse2 =  mydb1.cursor()
dbse2.execute('SELECT * FROM doctors WHERE patient_visited=0')
myresult2 = dbse.fetchall()
for q in myresult2:
    print("DOCTORS WITH NO PATIENT VISITED ARE:\n",q)