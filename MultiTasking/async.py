import asyncio

async def fetchData(delay):

    print("fetching something I guess")
    await asyncio.sleep(3)
    print("fetched some data o ye")
    return {"Data": "bla bla bla "}


async def sayhiTo():
    
    print("\nwell hello")
    task = fetchData(3)
    result = await task

    print(f"HEre is fetched data: {result}")
    print("Finitto ")
 


asyncio.run(sayhiTo())

