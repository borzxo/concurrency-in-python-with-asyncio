import asyncio
from aiohttp import ClientSession
from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)
        # print(f'All {status_codes}')
        # print(f'Accepted {[res for res in status_codes if not isinstance(res, Exception)]}')
        # print(f'Declined {[res for res in status_codes if isinstance(res, Exception)]}')

asyncio.run(main())
