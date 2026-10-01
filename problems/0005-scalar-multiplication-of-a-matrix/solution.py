# def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
# 	# Your code here
# 	pass

import numpy as np

def scalar_multiply(matrix, scalar) :
	return (np.asarray(matrix) * scalar).tolist()