import time
import multiprocessing



def calculateSquare(numbers,List):
    global squareList
    print("Calculating Square of numbers...")

    for index,value in enumerate(numbers):
        time.sleep(0.3)
        #print("Square of numbers: ", n * n)
        List[index] = value * value

def calculateCube(numbers,List):
    global cubeList
    print("Calculating Cube of numbers... ")

    for index,n in enumerate(numbers):
        time.sleep(0.3)
        #print("Cube is:", n * n * n)
        List[index]=n*n*n

if __name__ == "__main__":
    arr = [3, 5, 76, 34, 45, 81]

    t = time.time()
    squareList  = multiprocessing.Array('i',len(arr))
    cubeList = multiprocessing.Array('i',len(arr))
    # value = multiprocessing.Value('i',) i for index 

    p1 = multiprocessing.Process(target=calculateSquare, args=(arr, squareList))
    p2 = multiprocessing.Process(target=calculateCube, args=(arr, cubeList))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("The time has been spent:", time.time() - t)
    print("--------------------------------")
    print("This is square list:",squareList[:])
    print("This is cube list:",cubeList[:])