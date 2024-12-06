# def takeSquare(down):
#     def inner(up):
#         return down ** up

#     return inner

# #result = takeSquare(2)(3)
# #OR
# func = takeSquare(2)
# result =func(3)

#print(result)

# def askAutheration():
#     role=input("what is your role:")
#     def checkRole(role):
            
#         if role.lower() == "sudo":
#             return f"{role} is allowed to do anything"

#         else:
#             print("error: you cannot perform this operation without administrative privileges.")

#     return checkRole(role)

# result = askAutheration()
# print(result)

def calculate(nameofoperation):

    def addition(*args):
        sum = 0
        for i in args:
            sum +=i
        return sum

    def multi(*args):
        mut = 1
        for i in args:
            mut *=i
        return mut

    if nameofoperation=="Addition":
        return addition

    elif nameofoperation == "multiplication":
        return multi 
    else:
        return f"no such operation named {nameofoperation}"


nonsense = calculate("a nonsense value")
print(nonsense)
suma = calculate("Addition")
multip = calculate("multiplication")

result =suma(10,20)

print(result)
print
result = multip(10,20)
print(result)




