import numpy as np
import time

data_points, rows = 400_000_000, 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)

start = time.time()

result = np.mean(matrix, axis=1)

print(f'{(time.time() - start):.4f}')
