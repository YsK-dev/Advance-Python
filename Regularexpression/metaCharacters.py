import re

text = "A456r YsK 091 kps 479 @!' 900 74 Arfdh 32767 865454656 56867976478 t1q2"

# pattern = r"\d\d\d"
#pattern = r"\d+"
# pattern = r"\d*"
#pattern = r"\d{2}"
#pattern = r"\d{2,6}"
#pattern = r"\d{2,}"
#pattern = r"\d{,4}"
#pattern = r"\d.\d"
#pattern = r"[a-z]"
#pattern = r"\d|[a-z]"
#pattern = r"\d\w\w\w"
pattern = r"^A\d\w\w\w" #A456r
# matches = re.search(pattern, text)
#matches = re.findall(pattern, text)

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())

#print( matches)