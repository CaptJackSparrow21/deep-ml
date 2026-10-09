
import numpy as np
import math

def single_neuron_model(features, labels, weights, bias):
    z = np.dot(features, weights) + bias
    probabilities = 1 / (1 + np.exp(-z))
    mse = np.mean((probabilities - labels) ** 2)

    return np.round(probabilities, 4).tolist(), round(float(mse), 4)
