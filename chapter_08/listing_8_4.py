import asyncio
from util import delay


async def main():
    while True:
        delay_time = input('Input sleep time: ')
        asyncio.create_task(delay(int(delay_time)))


asyncio.run(main())
