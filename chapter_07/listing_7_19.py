import functools
import asyncio
import numpy as np
from concurrent.futures.thread import ThreadPoolExecutor
from util import async_timed


def mean_for_row(arr, row):
    return np.mean(arr[row])


data_points, rows = 400_000_000, 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = []
        for i in range(rows):
            mean = functools.partial(mean_for_row, matrix, i)
            tasks.append(loop.run_in_executor(pool, mean))

        results = asyncio.gather(*tasks)


asyncio.run(main())
