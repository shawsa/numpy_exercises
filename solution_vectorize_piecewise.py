'''Solutions to exercise_vectorize_piecewise.py'''

import numpy as np

def numpy_masking(X):
    A = np.empty_like(X, dtype=int)
    A[X<0.1] = 0
    A[np.logical_and(0.1 <= X, X < 0.5)] = 1
    A[0.5 <= X] = 2
    return A

def numpy_peicewise(X):
    return np.piecewise(X,
                        [X<0.1, np.logical_and(0.1<=X, X<.5), 0.5<=X],
                        [lambda x: 0, lambda x: 1, lambda x: 2])
