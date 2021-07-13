import json
#dict object type
x=[{"name":"tushar",
   "salary":35000.05,
   "permanent":True,
   "city":"pune"
    },
   {"name":"lucky",
   "salary":350000.05,
   "permanent":False,
   "city":"banglore"
   },
   {"name":"abhishek",
   "salary":100000.05,
   "permanent":True,
   "city":"chennai"
   },
   {"name":"omkaar",
   "salary":45200.05,
   "permanent":False,
   "city":"mumbai"
   }]
y=json.dumps(x)
z = json.loads(y)
print(z)
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8421436728",
)
dbse = mydb.cursor()
dbse.execute("DROP DATABASE IF EXISTS record_1")
dbse.execute("CREATE DATABASE record_1")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="8421436728",
    database="record_1"
)

dbse = mydb.cursor()
dbse.execute("DROP TABLE IF EXISTS employee_detail")
dbse.execute("CREATE TABLE employee_detail(name VARCHAR(255),salary DOUBLE,permanent VARCHAR(255),city VARCHAR(255))")
for i in json.dumps(y):
    sql_iinput = "INSERT INTO employee_detail(name,salary,permanent,city) VALUES((name),(salary),(permanent),(city))"
dbse.execute(sql_iinput)
mydb.commit()
print("inserted data")
