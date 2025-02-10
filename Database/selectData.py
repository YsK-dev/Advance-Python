import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)
cursor = db.cursor()

#sql = "SELECT * FROM products"
sql = "SELECT id,name FROM products" #better because I dont need other values yet 
cursor.execute(sql)

#productsResult=cursor.fetchall()

#for p in productsResult:
#    print(p[0],p[1])

productResult=cursor.fetchone()

print(productResult) #I cant use for loop beacuse I already fetched one :)