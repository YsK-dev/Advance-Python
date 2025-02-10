import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)
cursor = db.cursor()

def updateDatabyID(name,price,id):
    sql = "UPDATE products SET name=%s, price=%s WHERE id=%s"##  %40 is tax :)
    params=(name,price,id)

    cursor.execute(sql, params)
    try:
       
      db.commit()

      print(f"{cursor.rowcount}, is numbers of effected rows ")

    except mysql.connector.Error as e:
    
      print("oops Error -->",e)

    finally:
    
      cursor.close()
      db.close()

updateDatabyID("Huawei",13445434,4)