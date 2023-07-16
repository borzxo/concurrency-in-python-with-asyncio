import asyncio
import logging
from chapter_04 import fetch_status
from util import async_timed
from aiohttp import ClientSession


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = \
            [asyncio.create_task(fetch_status(session, 'python://bad.com')),
             asyncio.create_task(fetch_status(session, 'https://example.com', delay=3)),
             asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)
        print(f'Completed tasks {len(done)}')
        print(f'Pending tasks {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('An exception occurred while executing the request',
                              exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())
