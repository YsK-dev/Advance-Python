def filteration(fn, lists):
    result = []

    for item in lists:
        if fn(item):
            result.append(item)

    return result

def isEven(num):
    return num % 2 == 0

def isPositive(num):
    return num>0


numbers = [1,2,3,65,7,4,87,985,4576,-46,-3,-234,-34]

lastResult = filteration(isEven,numbers)

print(lastResult)

print("-------------------------")

lastResult = filteration(isPositive,numbers)

print(lastResult)