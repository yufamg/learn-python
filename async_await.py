import asyncio


async def fetch():
    await asyncio.sleep(2)
    return 777


# result = asyncio.run(fetch())
async def concurrent_fetch():
    return await asyncio.gather(fetch(), fetch(), fetch())


print()
results = asyncio.run(concurrent_fetch())

print(results)


async def timeoutFetch():
    return await asyncio.wait_for(fetch(), timeout=1)


try:
    waitforResult = asyncio.run(timeoutFetch())
    print(waitforResult)

except TimeoutError:
    print("TimeoutError")
