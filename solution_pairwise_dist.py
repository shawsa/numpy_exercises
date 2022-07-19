'''
A few solutions to the pairwise_dist.py exercise.
'''

import numpy as np
import numpy.linalg as la

def list_comp(X):
    '''Using a list comprehension instead of looping through indices.'''
    return np.array([[la.norm(xi - xj) for xj in X]
                     for xi in X])

def numpy_vectorized(X):
    return np.sqrt(sum(np.subtract.outer(x, x)**2
                       for x in X.T))

