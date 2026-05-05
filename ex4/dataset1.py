import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 真の関数の準備
def true_function(x):
    return np.sin(np.pi * x + 0.8) * 10


# 固定シードからランダム値を生成
def generate_random_by_seed(seed=10, n=20):
    rng = np.random.default_rng(seed)
    random_array = rng.uniform(-1, 1, n)
    return random_array


# 真の関数をプロットし保存
def plot_true_function_save(x, y):
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("真の関数")
    plt.legend()
    plt.savefig("ex4/ex1.1.png")


# サンプル集合を定義
def calc_sample_set(columns, min_n=-1, max_n=1, seed=10, n=20):
    rng = np.random.default_rng(seed)
    x = rng.uniform(min_n, max_n, n)
    y = true_function(x)
    temp = np.column_stack([x, y])
    df = pd.DataFrame(temp, columns)
    return df


# サンプル集合をプロットして保存
def plot_sample_set_and_save(df, xcolumn, ycolumn, path):
    plt.scatter(df[xcolumn], df[ycolumn])
    plt.savefig(path)


# ノイズを計算しDataFrameに追加
def calc_noise_and_apply(df, column, n=20, mu=0.0, sigma=np.sqrt(2.0), div=2):
    data = np.zeros(n)
    noise = np.random.normal(mu, sigma, n)
    half_noise = noise / div
    data = data + half_noise
    df[column] = data
    return df


# ノイズをプロットして保存
def plot_noise_and_save(df, xcolumn, ycolumn, path, color="red"):
    plt.scatter(df[xcolumn], df[ycolumn], c=color)
    plt.savefig(path)


def to_tsv(df):
    df.to_csv("./ex4/output.tsv", sep="\t", index=True)


def read_tsv(path):
    df = pd.read_csv(path, sep="\t")
    return df
