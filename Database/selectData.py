import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)
cursor = db.cursor()

sql = "SELECT * FROM products"

cursor.execute(sql)

productsResult=cursor.fetchall()

for p in productsResult:
    print(p[0],p[1])