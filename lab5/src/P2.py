import numpy as np
from icecream import ic


def CELoss_binary(X, y, theta):
    '''
    paras: X is a mini-batch of samples, y is the true label of the samples
        in the mini-batch, theta is the parameter we need to learn in logistic regression
    return: the binary cross entropy
    '''
    """Your code here"""
    z = X @ theta
    p = 1 / (1 + np.exp(-z))
    return -((np.log(p) * y) + np.log(1 - p) * (1 - y)).mean()


def precision(y_true, y_predict):
    '''
    paras: y_true is the true label, y_predict is the predicted label of your model
    return: the precision
    '''
    return np.sum(y_true == y_predict) / y_true.shape[0]


def gradient(X, y, theta):
    '''
    paras: X is a mini-batch of samples, y is the true label of the samples
        in the mini-batch, theta is the parameter we need to learn in logistic regression
    return: the mini-batch gradient of the binary cross entropy loss function with respect to 
        the parameter theta for a given mini-batch of samples
    '''
    """Your code here"""
    z = X @ theta
    p = 1 / (1 + np.exp(-z))
    grad = (p - y) @ X
    return grad / X.shape[0]


if __name__ == "__main__":
    X_all, y_all = np.load('Data2_X.npy'), np.load('Data2_Y.npy')
    """Your code here"""
    X_all_cat = np.hstack([X_all, np.ones([X_all.shape[0], 1])])

    lr, h = 0.1, 0.5
    batch_sizes = [1, 50, 100]
    epoch_num = 400
    loss = [[], [], []]
    acc = [[], [], []]
    ori_theta = np.random.random(X_all.shape[-1] + 1)
    for i, batch_size in enumerate(batch_sizes):
        theta = np.copy(ori_theta)
        for _ in range(epoch_num):
            indices = np.random.choice(
                np.arange(X_all_cat.shape[0]), batch_size, replace=False)
            X_batch = X_all_cat[indices]
            y_batch = y_all[indices]
            loss[i].append(
                ic(CELoss_binary(X_all_cat, y_all, theta)))
            acc[i].append(ic(precision(
                y_all, np.where(np.dot(X_all_cat, theta) > -np.log(1 / h - 1), 1, 0))))
            theta -= gradient(X_batch, y_batch, theta) * lr

    import matplotlib.pyplot as plt
    import matplotlib

    matplotlib.style.use("seaborn")

    fig, ax = plt.subplots(figsize=(5, 4))
    for y in loss:
        ax.plot(y)
    ax.legend([f"$batch\ size\ =\ {s}$" for s in batch_sizes])
    ax.set_title(f"$lr\ =\ {lr},\ h\ =\ {h}$")
    fig.savefig(f"loss_{lr}_{h}.png")

    fig, ax = plt.subplots(figsize=(5, 4))
    for y in acc:
        ax.plot(y)
    ax.legend([f"$batch\ size\ =\ {s}$" for s in batch_sizes])
    ax.set_title(f"$lr\ =\ {lr},\ h\ =\ {h}$")
    fig.savefig(f"acc_{lr}_{h}.png")

    fig, ax = plt.subplots(figsize=(5, 4))
    pos_index = np.where(y_all == 1)
    neg_index = np.where(y_all == 0)
    ax.scatter(
        X_all[pos_index, 0], X_all[pos_index, 1],
        marker='o', c="#EF4026")
    ax.scatter(
        X_all[neg_index, 0], X_all[neg_index, 1],
        marker='x', c="#069AF3")
    t = np.linspace(0, 1, 100)
    # theta[0] + theta[1] * x0 + theta[2] * x1 = -np.log(1 / h -1)
    y = - (np.log(1 / h - 1) + theta[0] * t + theta[2]) / theta[1]
    ax.plot(t, y, c="#15B01A")
    ax.set_title(f"$lr\ =\ {lr},\ h\ =\ {h}$")
    fig.savefig(f"all_{lr}_{h}.png")
