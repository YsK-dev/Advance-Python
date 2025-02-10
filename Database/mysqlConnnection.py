import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Asd171307.",
    database = "yskweb"


)

#print(db)

cursor = db.cursor()

#Creating a database o ye
#cursor.execute("CREATE DATABASE oYe")
#created database called oYe (o yeah) :)
#cursor.execute("SHOW DATABASES")

cursor.execute("CREATE TABLE categories(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")#adding one more table
cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)