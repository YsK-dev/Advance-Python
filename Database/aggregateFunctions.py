import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)

cursor = db.cursor()

#sql ="Select Count(*) from products"
#sql ="Select AVG(price) from products"
#sql ="Select SUM(price) from products"
#sql ="Select MIN(price) from products"
#sql ="Select max(price) from products"
#sql ="Select name,description from products where Price =(Select max(price) from products)"
#sql ="Select name,price from products ORDER BY price DESC"
sql = "Select name,price from products Order By price Desc Limit 1"

cursor.execute(sql)


result = cursor.fetchall()

print(result)