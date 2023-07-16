import asyncio


@asyncio.coroutine
def coroutine():
    print('Fall asleep!')
    yield from asyncio.sleep(1)
    print('Woke up!')


asyncio.run(coroutine())
