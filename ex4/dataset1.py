import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np


# 真の関数の準備
def true_function(x):
    return np.sin(np.pi * x + 0.8) * 10


def generate_graph():
    x = np.arange(-1, 1, 0.1)
# 真の関数をプロットし保存
def plot_true_function_save(x, y):
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("真の関数")
    plt.legend()
    plt.savefig("ex4/ex1.1.png")
    plt.plot(x, true_function(x))
    plt.show()


generate_graph()
