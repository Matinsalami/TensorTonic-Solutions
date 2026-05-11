import numpy as np


def function(x):
    return 1 / (1 + np.exp(x * (-1)))


def sigmoid(x):
    """
    Vectorized sigmoid function.
    """

    if type(x) in [int, float]:
        return function(x)

    
    x = np.asarray(x, dtype=float)
    
    return np.array([function(xi) for xi in x])

    
    