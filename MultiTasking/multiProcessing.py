import time
import multiprocessing

# Function to calculate the square of numbers and store the result in a shared list
def calculateSquare(numbers, List):
    print("Calculating Square of numbers...")

    # Iterate over the numbers and calculate the square
    for index, value in enumerate(numbers):
        time.sleep(0.3)  # Simulate a delay for demonstration purposes
        List[index] = value * value  # Store the result in the shared list

# Function to calculate the cube of numbers and store the result in a shared list
def calculateCube(numbers, List):
    print("Calculating Cube of numbers... ")

    # Iterate over the numbers and calculate the cube
    for index, n in enumerate(numbers):
        time.sleep(0.3)  # Simulate a delay for demonstration purposes
        List[index] = n * n * n  # Store the result in the shared list

if __name__ == "__main__":
    # Input list of numbers
    arr = [3, 5, 76, 34, 45, 81]

    # Start timing the execution
    t = time.time()

    # Create shared memory arrays to store the results
    squareList = multiprocessing.Array('i', len(arr))  # 'i' indicates integer type
    cubeList = multiprocessing.Array('i', len(arr))   # 'i' indicates integer type

    # Create two processes for parallel execution
    p1 = multiprocessing.Process(target=calculateSquare, args=(arr, squareList))
    p2 = multiprocessing.Process(target=calculateCube, args=(arr, cubeList))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    # Calculate and print the total time taken
    print("The time has been spent:", time.time() - t)
    print("--------------------------------")

    # Print the results stored in the shared lists
    print("This is square list:", squareList[:])  # Access the shared array using slicing
    print("This is cube list:", cubeList[:])      # Access the shared array using slicing