# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
# 	return means

import numpy as np

def calculate_matrix_mean(matrix, mode) :
	a = np.asarray(matrix, dtype = float)

	if mode == "row" :
		means = np.mean(a, axis = 1)
	else :
		means = np.mean(a, axis = 0)

	return means.tolist()