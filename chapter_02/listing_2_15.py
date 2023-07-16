import asyncio


def make_request() -> asyncio.Future:
    future = asyncio.Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


async def main():
    future = make_request()
    print(f'Is future object done? {future.done()}')
    value = await future
    print(f'Is future object done? {future.done()}')
    print(value)


asyncio.run(main())
