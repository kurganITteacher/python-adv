from random import randint
from time import perf_counter

import numpy as np
from random import randint
from time import perf_counter

import numpy as np

nums = [randint(1, 1000) for _ in range(10 ** 5)]

nums_by_7 = [num for num in nums]
start = perf_counter()
print(sum(nums_by_7), perf_counter() - start)

nums_by_7_np = np.array([num for num in nums]).astype('int64')
start = perf_counter()
print(sum(nums_by_7_np), perf_counter() - start)
# _sum = nums_by_7_np[0]  # int32
# _sum += nums_by_7_np[1]  # int32
# _sum += nums_by_7_np[2]  # int32
start = perf_counter()
print(nums_by_7_np.sum(), perf_counter() - start)

print(nums_by_7_np.mean(), sum(nums_by_7) / len(nums_by_7))
print(nums_by_7_np.std())
print(nums_by_7_np.min())
print(nums_by_7_np.max())
print(nums_by_7_np.size, nums_by_7_np.shape)
