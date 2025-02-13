import asyncio
import time

async def fetchData(id,delay):

    print("fetching something I guess this is id of that data:", id)
    await asyncio.sleep(3)
    print("fetched some data o ye id:",id)
    return {"ID": id, "Data": "bla bla bla "}


async def sayhiTo():
    task1 = fetchData(1,3)
    task2 = fetchData(2,2)
    task3 = fetchData(3,1)

    result1  = await task1
    print("here is the result: ", result1)

    result2  = await task2
    print("here is the result: ", result2)

    result3  = await task3
    print("here is the result: ", result3)


    
t = time.time()    
asyncio.run(sayhiTo())
print("the time is:", time.time() - t)




