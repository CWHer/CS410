import time

import matplotlib.pyplot as plt
import numpy as np

from utils import plot, prepare_data_sine


def ridge_regression(x, y, l2):
    # Normalize data.
    x = (x - x.mean(axis=-1, keepdims=True)) / x.std(axis=-1, keepdims=True)

    """Your code here"""
    y_pred = None  # predicted labels of size (n_samples, )
    intercept = None  # b of size ()
    coef = None  # theta of size (n_dims, )

    from sklearn import linear_model
    clf = linear_model.Ridge(alpha=l2)
    clf.fit(x, y)

    return clf.predict(x), clf.intercept_, clf.coef_


def lasso_regression(x, y, l1):
    # Normalize data.
    x = (x - x.mean(axis=-1, keepdims=True)) / x.std(axis=-1, keepdims=True)

    """Your code here"""
    y_pred = None  # predicted labels of size (n_samples, )
    intercept = None  # b of size ()
    coef = None  # theta of size (n_dims, )

    from sklearn import linear_model
    clf = linear_model.Lasso(alpha=l1)
    clf.fit(x, y)

    return clf.predict(x), clf.intercept_, clf.coef_


def main():
    # Prepare data.
    x, y = prepare_data_sine()
    plot(x[:, 0], y, 111)
    plt.show()

    # Set the different values of lambda to be tested.
    lambda_ridge = [1e-15, 1e-10, 1e-4, 1e-3, 1e-2, 5]
    plot_pos = [231, 232, 233, 234, 235, 236]

    for l2, pos in zip(lambda_ridge, plot_pos):
        start = time.time()
        y_pred, intercept, coef = ridge_regression(x, y, l2)
        time_cost = time.time() - start

        rss = sum((y_pred - y) ** 2)
        sparsity = np.mean(np.abs(coef) < 1e-7) * 100
        print(time_cost, rss, sparsity)

        plot(x[:, 0], y, pos, y_pred=y_pred,
             title=f"Ridge ($\lambda$={l2:.3g})")

    plt.show()

    # Set the different values of lambda to be tested.
    lambda_lasso = [1e-10, 1e-5, 1e-4, 1e-3, 1e-2, 1]
    plot_pos = [231, 232, 233, 234, 235, 236]

    for l1, pos in zip(lambda_lasso, plot_pos):
        start = time.time()
        y_pred, intercept, coef = lasso_regression(x, y, l1)
        time_cost = time.time() - start

        rss = sum((y_pred - y) ** 2)
        sparsity = np.mean(np.abs(coef) < 1e-7) * 100
        print(time_cost, rss, sparsity)

        plot(x[:, 0], y, pos, y_pred=y_pred,
             title=f"Lasso ($\lambda$={l1:.3g})")

    plt.show()


if __name__ == "__main__":
    main()
