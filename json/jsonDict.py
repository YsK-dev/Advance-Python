data = {
    "2":{
        "title": "Apple",
        "price": 5002,
    },
    "3":{
        "title":"Xiaomi",
        "price":3455,
    }
}

import json




with open("products.json") as files:
    products = json.load(files)

print(products["2"]) #{'title': 'Apple', 'price': 5002}

products.update({
    "1":{
        "title": "MAC mini",
        "price": 5075602,
    }
})
# print("\n------------------\n")
# #updated value
# print("Here is the updated value -->",final["2"]) #
with open("products.json","w",encoding="utf-8") as files:
    json.dump(products,files ,ensure_ascii=False,indent = 2)
