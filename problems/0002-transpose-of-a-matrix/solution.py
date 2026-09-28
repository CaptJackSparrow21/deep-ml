import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here

    
    A = np.asarray(a)
    n, m = A.shape
    T = np.zeros((m, n), dtype = A.dtype)
    for i in range(n) :
        for j in range(m) :
            T[j, i] = A[i, j]

    return T

    pass