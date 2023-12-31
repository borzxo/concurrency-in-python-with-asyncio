import asyncio
import aiohttp


async def fetch_status(session: aiohttp.ClientSession,
                       url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=.1)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://example.com')

asyncio.run(main())
