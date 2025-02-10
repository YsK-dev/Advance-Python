import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Asd171307.",
    database = "yskweb"
)

cursor = db.cursor()

sql = ("INSERT INTO products (name,price,imageurl,description) VALUES(%s,%s,%s,%s)")

#values=("Iphone 16","2000","apple.jpg","you should buy it has ai in it")
values= [("Iphone 17","2000","apple.jpg","you should buy it has ai in it"), ("Xiaomi14","1200","trash.jpg","it is fp phone but it has no quality in it")]


cursor.executemany(sql,values)

try:
    db.commit()
    print(cursor.rowcount, "RecordHas been saved 🥳")
    print(f"Id of Last added Record:{cursor.lastrowid}")
except mysql.connector.errors as e:
    print("The error is ",e)

finally:
    cursor.close()
    db.close()
    print("\n------------------------\nYOU MADE IT no bugs o ye")

