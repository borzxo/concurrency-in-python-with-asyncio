import asyncio
from util import *


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


@async_timed()
async def main():
    one = asyncio.create_task(cpu_bound_work())
    two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))
    await one
    await two
    await delay_task


asyncio.run(main())
