# def takeSquare(down):
#     def inner(up):
#         return down ** up

#     return inner

# #result = takeSquare(2)(3)
# #OR
# func = takeSquare(2)
# result =func(3)

#print(result)

def askAutheration():
    role=input("what is your role:")
    def checkRole(role):
            
        if role.lower() == "sudo":
            return f"{role} is allowed to do anything"

        else:
            print("error: you cannot perform this operation without administrative privileges.")

    return checkRole(role)

result = askAutheration()
print(result)
