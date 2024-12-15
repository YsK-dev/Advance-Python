import requests

respons = requests.post("https://jsonplaceholder.typicode.com/posts",data = {
    "userId":2,
    "title":"NEW POST sunt aut facere turi optio",
    "body":	"quia et suscipit\nsuscipit recusandae consequuntur expedita et cum"
})

result = respons

print(result)# 201 created 
print("\n_________________________________\n")
result = respons.text
print(result)