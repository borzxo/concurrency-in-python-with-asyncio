import asyncio
from util import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.TimeoutError:
        print("Task running more than 5 sec, soon it will complete!")
        result = await task
        print(result)

asyncio.run(main())
