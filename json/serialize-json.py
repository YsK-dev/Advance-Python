import json
product = {
        "id": 56,
        "title": "Macbook air 15.3",
        "price": "20000",
        "rating": "4.7",
        "category": "laptopım",
        "colours": ["grey","black","Space gray"]
}

print(product)
print(product["title"])
print(type(product))

print("\n-----------------------\n")
# result =json.dumps(product)

# print(result)
# print(type(result))

with open("product.json","w",encoding="utf-8") as file:
    json.dump(product,file,ensure_ascii=False,indent=2)