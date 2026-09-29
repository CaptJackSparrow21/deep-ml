import numpy as np

# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
def reshape_matrix(a, new_shape) :
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	try :
		return np.reshape(a, new_shape).tolist()
	except ValueError:
		return []

	return reshaped_matrix