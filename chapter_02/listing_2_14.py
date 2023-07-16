from asyncio import Future

my_future = Future()

print(f'my_future is ready? {my_future.done()}')

my_future.set_result(42)

print(f'my_future is ready? {my_future.done()}')

print(f'What result is in my_future? {my_future.result()}')
