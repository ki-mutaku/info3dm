import numpy as np


def load_linear_example1():
    """
    >>> import datasets
    >>> X,Y = datasets.load_linear_example1()
    >>> print(X[0])
    [1 4]
    """
    X = np.array([[1, 4], [1, 8], [1, 13], [1, 17]])
    Y = np.array([7, 10, 11, 14])
    return X, Y
