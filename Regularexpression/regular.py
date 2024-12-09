import re

text = "Best engineer Best best ever"
pattern ="Best"

matched =re.search(pattern, text)
result = matched
result = matched.start()
result = matched.end()

match = re.findall(pattern, text)
result = match

print(result)