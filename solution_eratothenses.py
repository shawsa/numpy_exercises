'''A numpy solution to exercise_eratosthenes.py'''

import numpy as np

def numpy_masking(upper_bound):
    nums = np.arange(2, upper_bound)
    primes = np.zeros_like(nums)
    index = 0
    while len(nums) > 0:
        primes[index] = nums[0]
        nums = nums[nums%primes[index] != 0]
        index += 1

    return primes[:index]
