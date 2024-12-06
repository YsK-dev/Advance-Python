def greet(name):
    return f" hi! {name}"

# print(greet("yusuf"))

hello = greet

print(greet)

print(hello)
print(greet("yakup"))
print(hello("rümeysa"))