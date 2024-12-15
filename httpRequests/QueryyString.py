import requests
import json
resp = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=false")

todos = resp.json()

result = todos# gettig todos that havent completed


print(result)
print("\n----------\n")
print(result[0]["title"])



