import re

text = "Yusuf sertkaya Python Javascript SQL html css c++  15-may-2025 15.may.2025 15/May/2015 21.06.2034 phone number +90-533-333-33-33  +90 544 001 00 00 yook +90.645.545.34.43 crazyengineer@gmail.net kodmaster@gmail.com"

#pattern = r"\d\d-[a-zA-z][a-zA-z][a-zA-z]-\d"
#pattern = r"\d{2}[-./][a-zA-Z0-9]{2,3}[-./]\d{4}"
#pattern = r"\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}"

#pattern = r"\w+@[a-z]+(\.[a-z]{2,3})+"

pattern = r"\+\d{2}[-\s\.]\d{3}-\d{3}[-\s\.]\d{2}[-\s\.]\d{2}"
matches = re.finditer(pattern, text)

for match in matches:
    print(match)

