import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'Finished counting to {count_to} in {end - start}')
    return counter


if __name__ == '__main__':
    with ProcessPoolExecutor() as process_pool:
        numbers = [1, 3, 4, 22, 1000000000]
        for r in process_pool.map(count, numbers):
            print(r)
