class Product:
    def __init__(self,id,title,price):
        self.id= id
        self.title=title
        self.price=price
#Serialize
# # p1 = Product(1,"SAmsung 47",854)
# # print(p1.__dict__)
# # prod = [p1.__dict__]
import json

# # with open("serializeProducts.json","w") as file:
# #      json.dump(prod,file)

# DEserialize
with open("serializeProducts.json") as file:
    prodData = json.load(file)

prodList = []
for item in prodData:
    prodList.append(Product(item["id"], item["title"], item["price"]))

# Print product titles
for product in prodList:
    print(product.title)