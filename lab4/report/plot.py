import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from icecream import ic
import pickle

data = dict()
rewards = ["0.01", "0.4", "2.0"]
for prefix in ["VI", "PI"]:
    data[prefix] = dict()
    for reward in rewards:
        with open("{}_{}.pkl".format(prefix, reward), "rb") as f:
            data[prefix][reward] = pickle.load(f)

states = [(0, 0),  (0, 1), (1, 0), (1, 1), (3, 0), (1, 3), (3, 2)]


def getValues(results, state):
    ret = []
    for result in results:
        ret.append(result[state])
    return ret


# ic(getValues(data["VI"]["0.01"], states[0]))

sns.set_theme(style="darkgrid")

for i in range(3):
    ax = plt.subplot(1, 3, i + 1)
    # ax.grid(True)

    results = data["VI"][rewards[i]]
    times = np.arange(len(results))
    for state in states:
        ax.plot(times, getValues(results, state),
                "-o", markersize=4, label=f"${state}$")

    ax.set_xlabel("$Number \ of \ iterations$")
    ax.set_ylabel("$Utility \ Estimation$")

    ax.set_title("$reward = -{}$".format(rewards[i]))

    # ax.set_ylim(min(datasets[data_name][item_mean]) - delta * 0.5,
    #             max(GCNN[i], max(datasets[data_name][item_mean])) + delta * 0.5)
    ax.legend()
    # plt.show()
plt.show()

for i in range(3):
    ax = plt.subplot(1, 3, i + 1)
    # ax.grid(True)

    results = data["PI"][rewards[i]]
    times = np.arange(len(results))
    for state in states:
        ax.plot(times, getValues(results, state),
                "-o", markersize=4, label=f"${state}$")

    ax.set_xlabel("$Number \ of \ iterations$")
    ax.set_ylabel("$Utility \ Estimation$")

    ax.set_title("$reward = -{}$".format(rewards[i]))

    # ax.set_ylim(min(datasets[data_name][item_mean]) - delta * 0.5,
    #             max(GCNN[i], max(datasets[data_name][item_mean])) + delta * 0.5)
    ax.legend()
    # plt.show()
plt.show()
print("done")
