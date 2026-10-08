import numpy as np
import math

def softmax(scores) :
    scores = np.array(scores)
    scores = scores - np.max(scores)

    exp_scores = np.exp(scores)
    return (exp_scores / np.sum(exp_scores)).tolist()