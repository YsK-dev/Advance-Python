import json 

data = [
    {
        "id":1,
        "title":"Macbook",
        "price":5003
    },
    {
        "id":2,
        "title":"samsung",
        "price": 4003
    }
]

# with open("product.json","w",encoding="utf-8") as file:
#     json.dump(data,file,ensure_ascii=False,indent=2)

product = {
    "id":3,
    "title":"huawei",
    "price":6500
}
with open("product.json") as file:
    products = json.load(file)

for i in products:
     if i["title"] == "huawei":
          i["title"] = "honor"
          print(i)

#products.append(product)

with open("product.json","w",encoding="utf-8") as file:
     json.dump(products,file,ensure_ascii=False,indent=2)
