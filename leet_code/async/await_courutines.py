import asyncio


async def nested():
    print(42)


async def main_coro():
    nested()
    await nested()


async def main_task():
    task = asyncio.create_task(nested())
    await task


if __name__ == '__main__':
    asyncio.run(main_coro())
