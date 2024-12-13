import json
#with open("/home/ysk/Desktop/advancePython/json/product.json") as file:
#    data = json.load(file)

#JSON string
data ="""
    {
        "id": 1,
        "title": "Macbook air",
        "price": "20000",
        "rating": "4.7",
        "category": "laptop",
        "colours": "grey"
    }
"""
data = json.loads(data)

print(data)
print(type(data))
print(data["title"])
print("the price is ",data["price"],"TL")
print(data["colours"])



# Deserialize --> decode

# Serialize -->encode
