
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot_vL = sum(a * b for a, b in zip(v, L))
	dot_LL = sum(x * x for x in L)

	scalar = dot_vL / dot_LL

	return [round(scalar * x, 3) for x in L]
