def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	n = len(matrix)
	a = [row[:] for row in matrix]

	trace = sum(a[i][i] for i in range(n))
	det = 1.0

	for i in range(n) :
		pivot = max(range(i, n), key = lambda r : abs(a[r][i]))

		if a[pivot][i] == 0 :
			det = 0.0
			break

		if pivot != i :
			a[i], a[pivot] = a[pivot], a[i]
			det *= -1

		value = a[i][i]
		det *= value

		for j in range(i + 1, n) :
			factor = a[j][i] / value

			for k in range(i + 1, n) :
				a[j][k] -= factor * a[i][k]

			a[j][i] = 0.0

	return (det, float(trace))












