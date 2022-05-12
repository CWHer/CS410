import time

import matplotlib.pyplot as plt
import numpy as np

from utils import plot, prepare_data_sine


def ridge_regression(x, y, lamda):
    # Normalize data.
    x = (x - x.mean(axis=-1, keepdims=True)) / x.std(axis=-1, keepdims=True)

    # Fit the model.
    from sklearn.linear_model import Ridge

    ridge_reg = Ridge(alpha=lamda)
    ridge_reg.fit(x, y)

    y_pred = ridge_reg.predict(x)
    intercept = ridge_reg.intercept_
    coef = ridge_reg.coef_

    return y_pred, intercept, coef

def lasso_regression(x, y, lamda):
    # Normalize data.
    x = (x - x.mean(axis=-1, keepdims=True)) / x.std(axis=-1, keepdims=True)

    # Fit the model.
    from sklearn.linear_model import Lasso

    lasso_reg = Lasso(alpha=lamda, max_iter=1e6)
    lasso_reg.fit(x, y)
    y_pred = lasso_reg.predict(x)

    y_pred = lasso_reg.predict(x)
    intercept = lasso_reg.intercept_
    coef = lasso_reg.coef_

    return y_pred, intercept, coef

def main():
    # Prepare data.
    x, y = prepare_data_sine()
    plot(x[:, 0], y, 111)
    plt.show()

    # Set the different values of lambda to be tested.
    lamda_ridge = [1e-15, 1e-10, 1e-4, 1e-3, 1e-2, 5]
    plot_pos = [231, 232, 233, 234, 235, 236]

    for lamda, pos in zip(lamda_ridge, plot_pos):
        start = time.time()
        y_pred, intercept, coef = ridge_regression(x, y, lamda)
        time_cost = time.time() - start

        rss = sum((y_pred - y) ** 2)
        sparsity = np.mean(np.abs(coef) < 1e-7) * 100
        print(time_cost, rss, sparsity)

        plot(x[:, 0], y, pos, y_pred=y_pred, title=f"Ridge ($\lambda$={lamda:.3g})")

    plt.show()

    # Set the different values of lambda to be tested.
    lamda_lasso = [1e-10, 1e-5, 1e-4, 1e-3, 1e-2, 1]
    plot_pos = [231, 232, 233, 234, 235, 236]

    for lamda, pos in zip(lamda_lasso, plot_pos):
        start = time.time()
        y_pred, intercept, coef = lasso_regression(x, y, lamda)
        time_cost = time.time() - start

        rss = sum((y_pred - y) ** 2)
        sparsity = np.mean(np.abs(coef) < 1e-7) * 100
        print(time_cost, rss, sparsity)

        plot(x[:, 0], y, pos, y_pred=y_pred, title=f"Lasso ($\lambda$={lamda:.3g})")

    plt.show()

if __name__ == "__main__":
    main()
