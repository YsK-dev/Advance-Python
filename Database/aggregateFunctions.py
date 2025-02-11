import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)

cursor = db.cursor()

#sql ="Select Count(*) from products"
sql ="Select AVG(price) from products"

cursor.execute(sql)


result = cursor.fetchone()

print(result)