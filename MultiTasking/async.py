import asyncio
import time

async def fetchData(id,delay):

    print("fetching something I guess this is id of that data:", id)
    await asyncio.sleep(3)
    print("fetched some data o ye id:",id)
    return {"ID": id, "Data": "bla bla bla "}


async def sayhiTo():
    results = await asyncio.gather(fetchData(1,3),fetchData(2,2),fetchData(3,1))

    for r in results:
        print("here is the results - ->",r)

    
t = time.time()    
asyncio.run(sayhiTo())
print("the time is:", time.time() - t)




