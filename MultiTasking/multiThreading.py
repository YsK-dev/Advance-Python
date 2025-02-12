import time
import threading as thr

def calculateSquare(numbers):
    print("Calculating Square of numbers...")

    for n in numbers:
        time.sleep(0.7)
        print("Square of numbers: ", n * n)

def calculateCube(numbers):
    print("Calcualting Cube of numbers... ")

    for n in numbers:
        time.sleep(0.7)
        print("Cube is:", n * n * n)

exNumbers=[1,4,6,7,8,2,3]
t =time.time()

#calculateSquare(exNumbers)
#calculateCube(exNumbers) # okey this works sychrnous so it is not what ı want

t1 = thr.Thread(target=calculateSquare,args=(exNumbers,)) #example numbers has to be tuple 
t2 = thr.Thread(target=calculateCube,args=(exNumbers,))

t1.start()
t2.start()

t1.join()
t2.join()
print("\n Calculation is over time taken is:",time.time() -t)