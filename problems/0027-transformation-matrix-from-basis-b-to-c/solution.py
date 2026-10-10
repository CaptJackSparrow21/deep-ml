import numpy as np

def transform_basis(B, C) :
	B = np.array(B)
	C = np.array(C)
	P = np.linalg.inv(C) @ B

	return P