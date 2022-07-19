#!/bin/python3

'''
Find all primes below an input integer using the seive of Eratosthenese. Return them
in a numpy array.
'''

import numpy as np
import numpy.linalg as la
import timeit

from solution_eratothenses import numpy_masking

def sol_check(upper_bound):
    primes = [2]
    for num in range(3, upper_bound):
        is_prime = True
        for p in primes:
            if num%p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return np.array(primes)


solution_list = [
        numpy_masking
    ]

'''
Code your own solution as a function with the same signature as the
function above, and add your solution to the list of solutions. Here's an
example below.
'''
# hint: use advanced indexing (masking)

def comprehensions(upper_bound):
    primes = [2]
    def filter_primes(num):
        is_prime = all(num%p != 0 for p in primes)
        if is_prime:
            primes.append(num)
        return is_prime
    return [2] + list(filter(filter_primes, range(3, upper_bound)))

solution_list.append(comprehensions)

if __name__ == '__main__':

    X = 10_000

    num_runs = 50
    repeats = 5

    print('Checking correctness...')
    A = sol_check(X)
    passed_list = []
    for my_sol in solution_list:
        passed = np.sum(np.abs(A - my_sol(X))) == 0.0
        if passed:
            print(f'{my_sol.__name__} is correct')
            passed_list.append(my_sol)
        else:
            print(f'{my_sol.__name__} failed')


    print('Timeing solutions...')
    base_time = np.average(timeit.repeat('sol_check(X)',
                                         globals=globals(),
                                         number=num_runs,
                                         repeat=repeats))
    print(f'The base solution ran in {base_time:.3f} seconds')
    for my_sol in passed_list:
        time = np.average(timeit.repeat(f'{my_sol.__name__}(X)',
                                         globals=globals(),
                                         number=num_runs,
                                         repeat=repeats))
        speedup = 100*(base_time / time - 1)
        print(f'{my_sol.__name__} ran in {time:.3f} seconds: {speedup:.1f}% faster than the base soltution.')

