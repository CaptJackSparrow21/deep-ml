def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    mn = min(x)
    mx = max(x)

    if mn == mx :
        return [0.0] * len(x)

    return [(i - mn) / (mx - mn) for i in x]