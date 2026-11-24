import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:

    h1 = np.maximum(0, np.dot(w1, x))
    h2 = np.dot(w2, h1)
    output = np.maximum(0, h2 + x)

    return output