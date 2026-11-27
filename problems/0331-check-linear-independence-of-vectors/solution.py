import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    if not vectors :
        return True

    a = [row[:] for row in vectors]
    m, n = len(a), len(a[0])

    rank = 0
    eps = 1e-9

    for col in range(n) :
        pivot = max(range(rank, m), key = lambda r : abs(a[r][col]), default = rank)

        if rank == m or abs(a[pivot][col]) < eps :
            continue
        
        a[rank], a[pivot] = a[pivot], a[rank]

        for r in range(rank + 1, m) :
            factor = a[r][col] / a[rank][col]

            for c in range(col, n) :
                a[r][c] -= factor * a[rank][c]

        rank += 1

        if rank == m :
            break

    return rank == m














