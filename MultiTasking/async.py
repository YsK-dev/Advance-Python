import asyncio

async def sayhiTo(name):
    
    print("\nwell hello")
    await asyncio.sleep(2)
    print(name)

coroutineObject = sayhiTo("yakup")

asyncio.run(coroutineObject)

