import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    B = A.T @ A
    p, q, r = B[0, 0], B[0, 1], B[1, 1]

    theta = 0.5 * np.arctan2(2 * q, p - r)
    c, s = np.cos(theta), np.sin(theta)
    V = np.array([[c, -s], [s, c]])

    D = V.T @ B @ V
    S = np.sqrt(np.maximum(np.diag(D), 0))

    order = np.argsort(S)[::-1]
    S, V = S[order], V[:, order]

    U = np.zeros((2, 2))
    tol = 1e-12

    for i in range(2) :
        if S[i] > tol :
            U[:, i] = A @ V[:, i] / S[i]
        elif i == 0 :
            U[:, i] = [1, 0]
        else :
           U[:, i] = [-U[1, 0], U[0, 0]]
        
    if S[0] <= tol :
        U = np.eye(2)
    
    return U, S, V.T
