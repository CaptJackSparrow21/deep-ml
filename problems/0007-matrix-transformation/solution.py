import numpy as np

def transform_matrix(A, T, S):
	A, T, S = map(np.array, (A, T, S))
	if (T.shape[0] != T.shape[1] or 
		S.shape[0] != S.shape[1] or 
		np.linalg.matrix_rank(T) < T.shape[0] or
		np.linalg.matrix_rank(S) < S.shape[0]) :
			return -1;

	transformed_matrix = np.linalg.inv(T) @ A @ S



	return transformed_matrix