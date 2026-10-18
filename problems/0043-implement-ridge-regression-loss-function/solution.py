import numpy as np

def ridge_loss(X, w, y_true, alpha) :
	y_pred = X @ w
	mse = np.mean((y_true - y_pred) ** 2)
	penalty = alpha * np.sum(w ** 2)
	return float(mse + penalty)
