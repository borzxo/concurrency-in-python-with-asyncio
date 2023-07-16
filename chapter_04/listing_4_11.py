import asyncio
import logging
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        good_request = fetch_status(session, 'https://example.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [asyncio.create_task(good_request),
                    asyncio.create_task(bad_request)]

        done, pending = await asyncio.wait(fetchers)

        print(f'Complete tasks: {done}')
        print(f'Pending tasks: {pending}')

        for done_task in done:
            # result await done_task will raise exception
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('An exception occurred while executing the request',
                              exc_info=done_task.exception())

asyncio.run(main())
