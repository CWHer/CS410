import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from icecream import ic

depth = [[1, 2, 3, 4, 5, 6, 7, 8], [0, 5, 10]]
memory = [[2, 3, 4, 5, 5, 5, 6, 7], [1, 5, 8]]
time = [[3, 6, 10, 16, 23, 30, 45, 12], [1, 23, 15]]
sns.set_theme(style="darkgrid")

types = ["depth=x", "depth=5x"]
for i in range(2):
    ax = plt.subplot(1, 2, 1)
    # ax.grid(True)

    ax.plot(depth[i], time[i],
            "-o", markersize=6, label=f"${types[i]}$")

    ax.set_xlabel("$depth$")
    ax.set_ylabel("$time$")

    ax.set_title("$time\ consumption$")

    # ax.set_ylim(min(datasets[data_name][item_mean]) - delta * 0.5,
    #             max(GCNN[i], max(datasets[data_name][item_mean])) + delta * 0.5)
    ax.legend()
    # plt.show()
for i in range(2):
    ax = plt.subplot(1, 2, 2)
    # ax.grid(True)

    ax.plot(depth[i], memory[i],
            "-o", markersize=6, label=f"${types[i]}$")

    ax.set_xlabel("$depth$")
    ax.set_ylabel("$memory$")

    ax.set_title("$memory\ consumption$")

    # ax.set_ylim(min(datasets[data_name][item_mean]) - delta * 0.5,
    #             max(GCNN[i], max(datasets[data_name][item_mean])) + delta * 0.5)
    ax.legend()
plt.show()
# plt.tight_layout()
# fig.autofmt_xdata(rotation=30)
