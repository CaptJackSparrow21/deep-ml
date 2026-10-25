import numpy as np

def calculate_eigenvalues(matrix):
	a, b = matrix[0]
	c, d = matrix[1]

	trace = a + d;
	determinant = a * d - b * c

	discriminant = trace ** 2 - 4 * determinant

	eigenvalues = [
		(trace + np.sqrt(discriminant)) / 2,
		(trace - np.sqrt(discriminant)) / 2
	]

	return sorted(eigenvalues, reverse = True)