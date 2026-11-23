def disorder(apples: list) -> float:
    """
    Compute the disorder in a basket of apples.
    """
    freq = {}

    for color in apples :
        freq[color] = freq.get(color, 0) + 1

    n = len(apples)
    gini = 1.0

    for count in freq.values() :
        p = count / n
        gini -= p * p

    return gini