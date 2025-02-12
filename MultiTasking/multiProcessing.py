import time
import multiprocessing

squareList  = []
cubeList = []

def calculateSquare(numbers):
    global squareList
    print("Calculating Square of numbers...")

    for n in numbers:
        time.sleep(0.3)
        #print("Square of numbers: ", n * n)
        squareList.append(n * n )

def calculateCube(numbers):
    global cubeList
    print("Calculating Cube of numbers... ")

    for n in numbers:
        time.sleep(0.3)
        #print("Cube is:", n * n * n)
        cubeList.append(n*n*n)

if __name__ == "__main__":
    arr = [3, 5, 76, 34, 45, 81]

    t = time.time()

    p1 = multiprocessing.Process(target=calculateSquare, args=(arr,))
    p2 = multiprocessing.Process(target=calculateCube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("The time has been spent:", time.time() - t)
    print("--------------------------------")

    t = time.time()

    calculateSquare(arr)

    calculateCube(arr)



    print("The time has been spent:", time.time() - t)
    print("This is square list:",squareList)
    print("This is cube list:",cubeList)