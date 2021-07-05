#create db connection and display version
import mysql.connector
myasd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='8421436728'
)
print(myasd)
import sys
cur = myasd.cursor()
cur.execute('SELECT VERSION()')
data = cur.fetchone()
print('DBMS Version :', str(data))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#create multiple table and insert data in it
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8421436728",
    database="mydatabase")
cur = mydb.cursor()
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS office")
cur.execute("CREATE TABLE customers(name VARCHAR(225) , address VARCHAR(225))")
cur.execute("CREATE TABLE office(employee_1 VARCHAR(225),salary_1 VARCHAR(225))")
sql = "INSERT INTO customers(name ,address) VALUES(%s , %s)"
val =("dhoni", "ranchi 7")
cur.execute(sql, val)
mydb.commit()
print(cur.rowcount, "  data successfully inserted in customer table")
sql_1 = "INSERT INTO office(employee_1 , salary_1)VALUES(%s,%s)"
val_1 = ("rohit", "25400")
cur.execute(sql_1, val_1)
mydb.commit()
print(cur.rowcount, "  data successfully inserted in office table")

#------------------------------------------------------------------------------------------------------------------------------------------------------------


#create employee table ,insert data and display employee name using for loop
import mysql.connector
mykbc = mysql.connector.connect(
    host="localhost",
    username="root",
    password="8421436728",
    database="mydatabase")
dur = mykbc.cursor()
dur.execute("DROP TABLE IF EXISTS employee_2")
dur.execute("CREATE TABLE employee_2(employee_name VARCHAR(225), employee_age VARCHAR(225))")
rop = "INSERT INTO employee_2(employee_name , employee_age) VALUES (%s , %s)"
rep = [
    ('ravi','25'),
    ('gourav','58'),
    ('raghav','64'),
    ('sahil','85'),
    ('abhishek','45')
]

dur.executemany(rop , rep)
mykbc.commit()
print(dur.rowcount,"was inserted")
dur.execute('SELECT employee_name FROM employee_2')
myresult = dur.fetchall()
for x in myresult:
    print(x)

