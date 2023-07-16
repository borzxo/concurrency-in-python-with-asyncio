import asyncio
from aiohttp import ClientSession
from chapter_04 import fetch_status


async def main():
    async with ClientSession() as session:
        url = 'https://example.com'
        api_a = fetch_status(session, url)
        api_b = fetch_status(session, url, delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending:
            if task is api_b:
                print('API B too slow, cancelling')
                task.cancel()

asyncio.run(main())
