import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Asd171307.",


)

#print(db)

cursor = db.cursor()

#Creating a database o ye
cursor.execute("CREATE DATABASE oYe")
#created database called oYe (o yeah) :)
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)