import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)

cursor = db.cursor()

#sql = "Select * From products"
#sql =  "Select name from categoriesProd"
#sql  = "Select * From products inner join categoriesProd on products.categoryid=categoriesProd.id"

sql  = "Select products.name,products.description,categoriesProd.name From products inner join categoriesProd on products.categoryid=categoriesProd.id"

cursor.execute(sql)
result  = cursor.fetchall()
print(result)