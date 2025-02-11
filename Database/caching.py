import mysql.connector

from cachetools import cached,TTLCache ## ttl is for time expired 
import time
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asd171307.",
    database="yskweb"
)
@cached(cache=TTLCache(maxsize=32,ttl=60))
def getProducts():
    cursor = db.cursor()

    sql="Select p.name from products p inner join categoriesProd c on p.categoryid=c.id Where price>1200"

    print("hi from sqeulll")

    cursor.execute(sql)

    return cursor.fetchall()



s = time.time()
print(getProducts())#fromsql
print("The time that past is:",time.time()-s)
print("--------------------------")

s = time.time()
print(getProducts())#from cache
print("The time that past is:",time.time()-s)
s = time.time()
print(getProducts())#from cache
print("The time that past is:",time.time()-s)
s = time.time()
print(getProducts())#from cache
print("The time that past is:",time.time()-s)
s = time.time()
print(getProducts())#from cache
print("The time that past is:",time.time()-s)


time.sleep(10)
print(getProducts())
