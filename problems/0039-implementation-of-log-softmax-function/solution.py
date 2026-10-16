import numpy as np

def log_softmax(scores) :
	scores = np.asarray(scores, dtype = float)
	scores = scores - np.max(scores)

	return scores - np.log(np.sum(np.exp(scores)))
