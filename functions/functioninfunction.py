# def greet(name):
#     return f" hi! {name}"

# # print(greet("yusuf"))

# hello = greet

# print(greet)

# print(hello)
# print(greet("yakup"))
# print(hello("rümeysa"))

# def outer(number):
#     print("this is outer speaking for")
#     def inner(number):
#         print(number)
    
#     inner(number)

# outer(10)
# #inner(30)

def factorial(number):
    
    if not isinstance(number,int):
        raise TypeError("you have to give me a number ")

    if not number >=0:
        raise ValueError("In order to calculate factorial you have to give me   a number :(")

    def innerFactorial(number):
        if number<=1:
            return 1

        return number * innerFactorial(number-1)

    return innerFactorial(number)

result = factorial(-4)

print(result)