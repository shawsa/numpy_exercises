'''
The goal of this exercise is to evaluate this piecewise function

f(x) = | 0 if x < 0.1,
       | 1 if 0.1 <= x < 0.5,
       | 2 if 0.5 <= x

element-wise on an input matrix.'''


from functools import reduce
from operator import mul
import numpy as np
import numpy.linalg as la
import timeit

def sol_check(X):

    def f(x):
        if x < 0.1:
            return 0
        elif x < .5:
            return 1
        else:
            return 2

    A = np.empty_like(X).ravel()
    for i, x in enumerate(X.ravel()):
        A[i] = f(x)
    return A.reshape(X.shape)

solution_list = []

'''
Code your own solution as a function with the same signature as the
function above, and add your solution to the list of solutions. Here's an
example below.
'''
# hint: use numpy.piecewise

def sol1(X):

    def f(x):
        if x < 0.1:
            return 0
        elif x < .5:
            return 1
        else:
            return 2

    A = np.array([f(x) for x in X.ravel()])
    return A.reshape(X.shape)

solution_list.append(sol1)

def sol2(X):

    def f(x):
        if x < 0.1:
            return 0
        elif x < .5:
            return 1
        else:
            return 2

    A = np.empty_like(X)
    for index, x in np.ndenumerate(X):
        A[index] = f(x)
    return A

solution_list.append(sol2)

from solution_vectorize_piecewise import numpy_masking, numpy_peicewise
solution_list += [numpy_masking, numpy_peicewise]

if __name__ == '__main__':

    dims = (51, 21, 13, 7)
    n = reduce(mul, dims)

    X = np.random.rand(n).reshape(*dims)

    A = sol_check(X)
    passed_list = []
    print('Checking for correctness ...')
    for my_sol in solution_list:
        passed = la.norm((A - my_sol(X)).ravel()) < (5e-16 * n**2)
        if passed:
            print(f'{my_sol.__name__} is correct')
            passed_list.append(my_sol)
        else:
            print(f'{my_sol.__name__} failed')

    num_runs = 100
    repeats = 5

    print('Timing solutions ...')
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

