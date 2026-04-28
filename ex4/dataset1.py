import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np


def true_function(x):
    return np.sin(np.pi * x + 0.8) * 10


def generate_graph():
    x = np.arange(-1, 1, 0.1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, true_function(x))
    plt.show()


generate_graph()
