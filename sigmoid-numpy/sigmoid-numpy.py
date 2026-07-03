import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    #normalise inputs
    x = np.asarray(x, dtype = float)
    # calculate and return
    return 1 / (1 + np.exp(-x))