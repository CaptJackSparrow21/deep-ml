
import numpy as np

def gini_impurity(y):
    """
    Calculate Gini Impurity for a list of class labels.

    :param y: List of class labels
    :return: Gini Impurity rounded to three decimal places
    """
    n = len(y)
    if n == 0 :
        return 0.0

    freq = {}

    for x in y :
        freq[x] = freq.get(x, 0) + 1

    gini = 1

    for count in freq.values() :
        p = count / n
        gini -= p ** 2

    return round(gini, 3)