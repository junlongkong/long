import asyncio
import time
async def async_test(delay:int,content):
    await asyncio.sleep(delay)
    print(content)

if __name__ == '__main__':
    print(f"start at {time.strftime('%X')}")
    asyncio.run(asyncio.wait([async_test(1,"lady"),async_test(2,"killer")]))
    print(f"end at {time.strftime('%X')}")
