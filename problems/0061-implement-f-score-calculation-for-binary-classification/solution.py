
import numpy as np

def f_score(y_true, y_pred, beta):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0

    b2 = beta ** 2
    denominator = b2 * precision + recall

    if denominator == 0:
        return 0.0

    return round((1 + b2) * precision * recall / denominator, 3)
