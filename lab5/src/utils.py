import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons


########## Calculation ##########
def onehot_encoding(label, max_num_class):
    encoding = np.eye(max_num_class)
    encoding = encoding[label]

    return encoding

def calculate_acc(logits, label):
    correct = np.sum(np.argmax(logits, axis=1) == label)

    return correct / len(label)

########## Data ##########
def data_iterator(x, y, batch_size, shuffle=True):
    indx = list(range(len(x)))
    if shuffle:
        np.random.shuffle(indx)

    for start_idx in range(0, len(x), batch_size):
        end_idx = min(start_idx + batch_size, len(x))
        yield x[indx[start_idx: end_idx]], y[indx[start_idx: end_idx]]

def prepare_data_moons():
    x, y = make_moons(n_samples=1000, noise=0.2, random_state=100)

    return x, y

def prepare_data_sine():
    x = np.array([i * np.pi / 180 for i in range(60, 300, 4)])
    y = np.sin(x) + np.random.normal(0, 0.15, len(x))
    x = np.concatenate([x.reshape(-1, 1) ** i for i in range(1, 17)], axis=1)

    return x, y

########## Plotting ##########
def plot(x, y, pos, y_pred=None, title=None):
    plt.subplot(pos)
    plt.tight_layout()
    plt.plot(x, y, ".")

    if y_pred is not None:
        plt.plot(x, y_pred)
    if title is not None:
        plt.title(title)

def plot_decision_boundary(x, y, pred_func=None):
    """Plot a decision boundary."""
    # Set min and max values and give it some padding.
    x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
    y_min, y_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5
    h = 0.01

    # Generate a grid of points with distance h between them.
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    if pred_func is not None:
        # Predict the function value for the whole grid.
        Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        # Plot the contour and training examples.
        plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)

    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Spectral)
