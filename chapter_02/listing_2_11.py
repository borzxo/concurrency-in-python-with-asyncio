import asyncio
from util import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print('Task not ended, next check after 1 sec.')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print("Our task was cancelled")

asyncio.run(main())
