import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


coroutine_result = asyncio.run(coroutine_add_one(1))

print(f'Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}')