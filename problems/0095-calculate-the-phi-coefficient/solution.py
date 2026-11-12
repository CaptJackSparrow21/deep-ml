import math

def phi_corr(x: list[int], y: list[int]) -> float:
    """
    Calculate the Phi coefficient between two binary variables.

    Args:
    x (list[int]): A list of binary values (0 or 1).
    y (list[int]): A list of binary values (0 or 1).

    Returns:
    float: The Phi coefficient rounded to 4 decimal places.
    """
    # Your code here

    x00 = sum(1 for a, b in zip(x, y) if a == 0 and b == 0)
    x01 = sum(1 for a, b in zip(x, y) if a == 0 and b == 1)
    x10 = sum(1 for a, b in zip(x, y) if a == 1 and b == 0)
    x11 = sum(1 for a, b in zip(x, y) if a == 1 and b == 1)

    numerator = x00 * x11 - x01 * x10

    denominator = math.sqrt((x00 + x01) * (x10 + x11) * (x00 + x10) * (x01 + x11))

    if denominator == 0 :
        return 0.0

    return round(numerator / denominator, 4)











