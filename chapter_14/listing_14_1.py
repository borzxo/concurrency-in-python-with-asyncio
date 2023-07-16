import asyncio


class TaskRunner:

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.tasks = []

    def add_task(self, func):
        self.tasks.append(func)

    async def _run_all(self):
        awaitable_tasks = []

        for t in self.tasks:
            if asyncio.iscoroutinefunction(t):
                awaitable_tasks.append(asyncio.create_task(t()))
            elif asyncio.iscoroutine(t):
                awaitable_tasks.append(asyncio.create_task(t))
            else:
                self.loop.call_soon(t)

        await asyncio.gather(*awaitable_tasks)

    def run(self):
        self.loop.run_until_complete(self._run_all())


if __name__ == '__main__':

    def regular_function():
        print('Hello from a regular function!')

    async def coroutine_function():
        print('Running coroutine, sleeping!')
        await asyncio.sleep(1)
        print('Finished sleeping!')

    runner = TaskRunner()
    runner.add_task(coroutine_function)
    runner.add_task(coroutine_function())
    runner.add_task(regular_function)

    runner.run()
