import numpy as np

def check_relu(x):

    if x >= 0.0:
        return float(x)
    else:
        return 0.0



def relu(x):
    """
    Implement ReLU activation function.
    """
    if type(x) in [int, float]:
        return check_relu(x)

    x = np.asarray(x , dtype = float)
    vec = np.vectorize(check_relu)
    return np.array(vec(x))