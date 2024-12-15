import requests
import json

resp = requests.get("https://jsonplaceholder.typicode.com/posts")

result = resp
result = type(resp)
result = resp.status_code
result = resp.headers
result = resp.headers["Content-Type"]
result = resp.url
result = resp.encoding
result = resp.text
result = type(resp.text)
posts = json.loads(resp.text)
result = posts[0]["title"]

#print(result)

for item in posts:
    if item["userId"] ==1:
        print(item["title"])


