import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f'Started at {time.strftime("%X")}')
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f'Finished at {time.strftime("%X")}')


async def concurrent_main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f'Started at {time.strftime("%X")}')

    await task1
    await task2
    print(f'Finished at {time.strftime("%X")}')


if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(concurrent_main())
