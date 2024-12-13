db = {
    "users":{
        "YsK":{
            "firstName":"Yusuf",
            "lastName": "Sertkya",
        },
        "YK":{
            "firstName":"Yakup",
            "lastName": "Sertkya",
        },


    },
    "products":{
        "3": {
            "title": "Ultra",
            "price": 3455
        },
        "1": {
            "title": "Evil corp",
            "price": 5075602
}}}

import json

# with open("db.json","w",encoding="utf-8") as file:
#     json.dump(db,file,ensure_ascii=False,indent=2)

with open("db.json") as file:
    databeyz = json.load(file)

print(databeyz["users"]["YsK"])# Search for the user "Ysk"
print("Here is my lovely brand --> ",databeyz["products"]["3"]["title"])

db["products"].update({
    "1":{
        "title": "Apple",
        "price": 507992895602,

    }
})
print("Here is my new brand --> ",databeyz["products"]["1"]["title"])
with open("db.json","w",encoding="utf-8") as file:
      json.dump(db,file,ensure_ascii=False,indent=2)

