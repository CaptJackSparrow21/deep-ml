import numpy as np
import math

def sigmoid(z: float) -> float:
	#Your code here
	result = 1 / (1 + np.exp(-z))
	return result