# def createNumber():
#     num = 0
#     while True:
#         yield num ** 2
#         num +=1

# generator = createNumber()

# for i in generator:
#     print(i)


def fiboList(max):
    numbers = []

    a, b = 0,1


    while len(numbers) <= max:
        numbers.append(b)
        a,b =b,a+b

    return numbers

#print(fiboList(15))

def fiboGen(max):
    a, b=0,1
    counter = 0

    while counter <= max:
        a,b=b,a+b

        yield b

        counter += 1
 
# fiboGenerator = fiboGen(66)
# for i in fiboGenerator:
#     print(i)

import sys
listGen = [i for i in range(10000)]

print(sys.getsizeof(listGen))
print("------------------------")
gen = (i for i in range(10000))

print(sys.getsizeof(gen))
print("------------------------")

import time 

listStartTime = time.time()
sum([i for i in range(900000)])
listStop = time.time() - listStartTime

print("-----------------------")

genStartTime = time.time()
sum((i for i in range(900000)))
genStop = time.time() - genStartTime

print(listStop)
print("---------------------")
print(genStop)