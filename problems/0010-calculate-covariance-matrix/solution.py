# def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
# 	# Your code here
# 	return []

import numpy as np

def calculate_covariance_matrix(vectors) :
	return np.cov(vectors).tolist()