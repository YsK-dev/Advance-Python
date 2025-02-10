import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)

cursor = db.cursor()

#sql=("SELECT * FROM products WHERE id=1")
#sql=("SELECT * FROM products WHERE id>=1")
#sql=("SELECT * FROM products WHERE name='Iphone 17' or price='200'")
#sql=("SELECT * FROM products WHERE name LIKE '%Iphone%'")
#sql=("SELECT * FROM products WHERE name LIKE 'Xiaomi%'")
#sql=("SELECT * FROM products WHERE name LIKE '%Samsung' ")
#sql=("SELECT * FROM products WHERE name LIKE '%Samsung' and description LIKE '%phone%' ")

def getProductsbyId(id):
    sql=("SELECT * FROM products where id='%s'")
    params = (id,)
    cursor.execute(sql,params)

    filteredResult=cursor.fetchall()
    print(filteredResult)


getProductsbyId(7)