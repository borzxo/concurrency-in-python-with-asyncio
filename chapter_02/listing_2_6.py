import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'Fall asleep on {delay_seconds} sec.')
    await asyncio.sleep(delay_seconds)
    print(f'Finishing sleep for {delay_seconds} sec.')
    return delay_seconds
