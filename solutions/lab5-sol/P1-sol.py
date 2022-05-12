import numpy as np
from icecream import ic

def get_hat_matrix(x):
    return np.dot(np.dot(x, np.linalg.inv(np.dot(x.T, x))), x.T)

def get_theta_hat(X, y):
    return np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)

def L2(x):
    return np.sum(x**2)

if __name__ == "__main__":
    X = np.load('Data1_X.npy')
    t1 = np.dot(X.T, X)

    Y = np.load('Data1_Y.npy')
    Y_hat = np.dot(get_hat_matrix(X), Y) 
    ic(Y_hat)

    Y, Y_hat = Y.reshape(X.shape[0]), Y_hat.reshape(X.shape[0])
    ic(np.dot(X.T, (Y-Y_hat)))


