from bs4 import BeautifulSoup

with open("ysk.html") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser") 

result = obj

result = type(result)

result = obj.prettify()#to make it more clear
result = obj.title
result = type(obj.title)
result = obj.title.name
result = obj.title.string
result = obj.body
result = obj.body.h1
result = obj.body.h1.string
result = obj.h1.string
result = obj.div
result = obj.h2
print(result)