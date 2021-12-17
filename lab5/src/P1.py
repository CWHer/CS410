import numpy as np
from icecream import ic

if __name__ == "__main__":
    X = np.load('Data1_X.npy')
    Y = np.load('Data1_Y.npy')
    """Your code here"""
    Y_hat = X @ np.linalg.inv((X.T @ X)) @ X.T @ Y
    ic(Y_hat)

    Y_perp = Y - Y_hat
    for i in range(5):
        x = X[:, i].reshape(-1, 1)
        ic(np.vdot(x, Y_perp))
