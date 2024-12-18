from bs4 import BeautifulSoup

with open("ysk.html") as file:
    html = file.read()


obj = BeautifulSoup(html, "html.parser")

result = obj.find(id="item1")

result = obj.find(id="header")

result = obj.find(class_="section")

print(result)

