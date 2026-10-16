"""
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
"""

import numpy as np

def linear_regression_gradient_descent(X, y, alpha,iterations) :
    
    m, n = X.shape
    y = y.reshape(-1, 1)  
    theta = np.zeros((n, 1))  

    for _ in range(iterations):

        predictions = X @ theta

        error = predictions - y

        gradient = (X.T @ error) / m

        theta = theta - alpha * gradient


    return theta.flatten()