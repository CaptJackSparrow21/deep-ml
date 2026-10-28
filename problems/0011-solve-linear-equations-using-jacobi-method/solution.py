import numpy as np
def solve_jacobi(A, b, n) :
	A = np.array(A, dtype = float)
	b = np.array(b, dtype = float)

	x = np.zeros(len(b))

	for _ in range(n) :
		x_new = (b - (A @ x - np.diag(A) * x)) / np.diag(A)
		x = x_new

	return x