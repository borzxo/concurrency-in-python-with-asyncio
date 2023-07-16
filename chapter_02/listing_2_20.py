import asyncio
import requests
from util import *


@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.example.com').status_code


@async_timed()
async def main():
    one = asyncio.create_task(get_example_status())
    two = asyncio.create_task(get_example_status())
    three = asyncio.create_task(get_example_status())
    await one
    await two
    await three

asyncio.run(main())
