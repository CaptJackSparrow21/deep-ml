# import numpy as np
# def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
# 	# Your code here, make sure to round
# 	return theta

import numpy as np

def linear_regression_normal_equation(X, y):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    theta = np.linalg.pinv(X.T @ X) @ X.T @ y

    return np.round(theta, 4).tolist()