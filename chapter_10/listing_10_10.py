import asyncio
from chapter_10.listing_10_9 import retry, TooManyRetires


async def main():
    async def always_fail():
        raise Exception('I have failed!')

    async def always_timeout():
        await asyncio.sleep(1)

    try:
        await retry(always_fail,
                    max_reties=3,
                    timeout=.1,
                    retry_interval=.1)
    except TooManyRetires:
        print('Retried too many times!')

    try:
        await retry(always_timeout,
                    max_reties=3,
                    timeout=.1,
                    retry_interval=.1)
    except TooManyRetires:
        print('Retried too many times!')


asyncio.run(main())
