import numpy as np
import math
from tqdm import tqdm
from icecream import ic
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def CELoss_binary(X, y, theta):
    '''
    paras: X: (n_samples, n_features)
    '''
    return -y * np.log(sigmoid(np.dot(X, theta)) + np.finfo(np.float32).eps) - (1 - y) * np.log(1 - sigmoid(np.dot(X, theta)) + np.finfo(np.float32).eps)

def precision(y_true, y_predict):
    return np.sum(y_true == y_predict) / y_true.shape[0]

def gradient(X, y, theta):
    '''
    paras: X: (n_samples, n_features)
    '''
    return np.dot(X.T, sigmoid(np.dot(X, theta)) - y) / X.shape[0]

if __name__ == "__main__":

    n_ite, eta = 1000, 0.1
    X_train, y_train = np.load('Data2_X.npy'), np.load('Data2_Y.npy')
    ic(X_train, y_train)
    n, m = X_train.shape
    bs = 50 # batch size
    theta_hat = np.ones(m) / 2

    for ite in tqdm(range(n_ite)):
        loss = CELoss_binary(X_train, y_train, theta_hat)
        predict = sigmoid(np.dot(X_train, theta_hat)) > 1/2
        ic(ite, np.sum(loss))
        ic(precision(y_train, predict))
        samplie_idx = np.random.choice(n, bs, replace = False)
        theta_hat -= eta * gradient(X_train[samplie_idx], y_train[samplie_idx], theta_hat)
    