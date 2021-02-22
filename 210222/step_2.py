from random import randint
from sys import getsizeof

import numpy as np

# print(numpy.__version__)
# print(os.get_exec_path())

nums = [randint(1, 1000) for _ in range(10 ** 5)]

nums_by_7 = [num for num in nums if not num % 7]
print(type(nums_by_7), nums_by_7[3], getsizeof(nums_by_7))
nums_by_7_np = np.array([num for num in nums if not num % 7])
print(type(nums_by_7_np), nums_by_7_np[3],
      getsizeof(nums_by_7_np), nums_by_7_np.dtype)
nums_by_7_np_opt = nums_by_7_np.astype('uint16')
# nums_by_7_np_opt = nums_by_7_np.astype('uint8')
print(type(nums_by_7_np_opt), nums_by_7_np_opt[3],
      getsizeof(nums_by_7_np_opt), nums_by_7_np_opt.dtype)


