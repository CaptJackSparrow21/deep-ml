def calculate_f1_score(y_true, y_pred):
    """
    Calculate the F1 score based on true and predicted labels.

    Args:
        y_true (list): True labels (ground truth).
        y_pred (list): Predicted labels.

    Returns:
        float: The F1 score rounded to three decimal places.
    """
    tp = fp = fn = 0

    for actual, predicted in zip(y_true, y_pred) :
        if actual == 1 and predicted == 1 :
            tp += 1
        elif actual == 0 and predicted == 1 :
            fp += 1
        elif actual == 1 and predicted == 0 :
            fn += 1

    denominator = 2 * tp + fp + fn

    if denominator == 0 :
        return 0.0

    f1 = (2 * tp) / denominator

    return round(f1, 3)