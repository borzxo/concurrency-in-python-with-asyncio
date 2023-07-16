import asyncio
from asyncio import BoundedSemaphore


async def main():
    s = BoundedSemaphore(1)

    await s.acquire()
    s.release()
    s.release()


asyncio.run(main())
