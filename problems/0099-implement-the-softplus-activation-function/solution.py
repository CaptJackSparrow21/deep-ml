import math
import numpy as np

def softplus(x: float) -> float:
    """
    Compute the softplus activation function.

    Args:
        x: Input value

    Returns:
        The softplus value log(1 + e^x), rounded to 4 decimal places
    """

    # e = 2.71828
    # val = math.log(1 + (e ** x))
    # return round(val,4)

    return max(0, x) + np.log1p(np.exp(-abs(x)))