import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)

cursor = db.cursor()
def deleteProduct(id):
    sql ="DELETE FROM products WHERE id=%s"
    #sql ="DELETE FROM products WHERE name LIKE '%Samsung%'"
    params=(id,)

    cursor.execute(sql,params)

    try:
        db.commit()
        print(f"{cursor.rowcount} record deleted")

    except mysql.connector.Error as e:
        print("LOOK there is bug",e)

    finally:
        db.close()
        cursor.close()


deleteProduct(14)