#!/bin/python3

'''
Given an n x d matrix X, where each row of X denotes a point in R^d, 
compute the n x n matrix of pairwise distances A_ij = ||x_i, x_j||
where || denotes the Euclidean distance in R^d.
'''

import numpy as np
import numpy.linalg as la
from itertools import product
import timeit

from solution_pairwise_dist import list_comp, numpy_vectorized

def sol_check(X):
    n, d = X.shape
    A = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            A[i,j] = la.norm(X[i] - X[j])
    return A

solution_list = [
        list_comp,
        numpy_vectorized
    ]

'''
Code your own solution as a function with the same signature as the
function above, and add your solution to the list of solutions. Here's an
example below.
'''
# hint: use numpy.subtract.outer

def sol1(X):
    '''Not a great solution, just demonstrating something different.'''
    n, d = X.shape
    A = np.empty((n, n))
    for (i, xi), (j, xj) in product(enumerate(X),
                                    enumerate(X)):
        A[i, j] = la.norm(xi - xj)
    return A

solution_list.append(sol1)

if __name__ == '__main__':

    n = 100
    d = 3

    num_runs = 50
    repeats = 5

    X = np.random.rand(n*d).reshape(n, d)

    A = sol_check(X)
    passed_list = []
    for my_sol in solution_list:
        passed = la.norm(A - my_sol(X), ord='fro') < (5e-16 * n**2)
        if passed:
            print(f'{my_sol.__name__} is correct')
            passed_list.append(my_sol)
        else:
            print(f'{my_sol.__name__} failed')


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

