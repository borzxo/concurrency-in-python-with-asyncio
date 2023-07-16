import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = \
            [asyncio.create_task(fetch_status(session, 'https://example.com')),
             asyncio.create_task(fetch_status(session, 'https://example.com'))]
        done, pending = await asyncio.wait(fetchers)

        print(f'Done tasks: {len(done)}')
        print(f'Pending tasks: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)

asyncio.run(main())
