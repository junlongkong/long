import asyncio
import time
async def async_test(delay:int,content):
    await asyncio.sleep(delay)
    print(content)

async def main():
    task_lady = asyncio.create_task(async_test(1,"lady"))
    task_killer = asyncio.create_task(async_test(2,"killer9"))
    await task_killer
    await task_lady

if __name__ == '__main__':
    print(f"start at {time.strftime('%X')}")
    asyncio.run(main())
    print(f"end at {time.strftime('%X')}")
