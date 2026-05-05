import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def true_function(x):
    """真の関数を準備する関数

    y = sin(pi * x * 0.8) * 10 の結果を返す関数を定義する

    :param x: 入力x
    :return 真の関数の出力y

    >>> print(true_function(0))
    7.173560908995228
    """
    return np.sin(np.pi * x + 0.8) * 10


def plot_true_function_save(x, y, path, xlabel="x", ylabel="y", title="真の関数"):
    """真の関数をプロットして保存する

    true_function専用のプロット関数。演習1.1の関数化。

    :param x: 定義域
    :param y: 真の関数
    :param string path: グラフを出力するパス
    :param string xlabel: x軸のラベル (default: "x")
    :param string ylabel: y軸のラベル (default: "y")
    :param string title: グラフのタイトル (default: "真の関数")
    """
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.savefig(path)


def calc_sample_set(columns=["観測点", "真の値"], min_n=-1, max_n=1, seed=10, n=20):
    """サンプル集合を定義

    一様分布で定義された乱数のサンプル集合を定義する

    :param list columns: DataFrameにつける列名 (default: ["観測点", "真の値"])
    :param min_n: 一様分布の最小値 (default: -1)
    :param max_n: 一様分布の最大値 (default: 1)
    :param int seed: 一様分布のシード値 (default: 10)
    :param int n: 一様分布乱数の個数 (default: 20)
    :return: サンプル集合のDataFrame
    :rtype: pandas.core.frame.DataFrame
    """
    rng = np.random.default_rng(seed)
    x = rng.uniform(min_n, max_n, n)
    y = true_function(x)
    temp = np.column_stack([x, y])
    df = pd.DataFrame(temp, columns)
    return df


def plot_sample_set_and_save(df, xcolumn, ycolumn, path):
    """サンプル集合をプロットして保存する

    サンプル集合を散布図でプロットする

    :param pandas.core.frame.DataFrame df: サンプル集合のDataFrame
    :param string xcolumn: x軸に設定するDataFrameのカラム
    :param string ycolumn: y軸に設定するDataFrameのカラム
    :param string path: グラフを保存するパス
    """
    plt.scatter(df[xcolumn], df[ycolumn])
    plt.savefig(path)


def calc_noise_and_apply(df, column, n=20, mu=0.0, sigma=np.sqrt(2.0), div=2):
    """ノイズを計算しDataFrameに追加する

    正規分布の乱数を生成し、ノイズとする

    :param pandas.core.frame.DataFrame df: ノイズを追加したいDataFrame
    :param string column: ノイズの列名
    :param int n: 正規分布乱数の個数 (default: 20)
    :param float mu: 正規分布の平均値 (default: 0.0)
    :param float sigma: 正規分布の偏差 (default: np.sqrt(2.0))
    :param div: ノイズの割る数
    :return: ノイズ列が追加されたDataFrame
    :rtype: pandas.core.frame.DataFrame
    """
    data = np.zeros(n)
    noise = np.random.normal(mu, sigma, n)
    half_noise = noise / div
    data = data + half_noise
    df[column] = data
    return df


# ノイズをプロットして保存
def plot_noise_and_save(df, xcolumn, ycolumn, path, color="red"):
    """ノイズをプロットして保存する

    散布図でプロットする。デフォルトは赤の丸点。

    :param pandas.core.frame.DataFrame df: プロット対象のDataFrame
    :param string xcolumn: x軸のDataFrameカラム
    :param string ycolumn: y軸のDataFrameカラム
    :param string path: グラフの出力パス
    :param string color: 散布図のドットの色 (default: "red")
    """
    plt.scatter(df[xcolumn], df[ycolumn], c=color)
    plt.savefig(path)


def to_tsv(df):
    """DataFrameをtsv形式に変換する

    :param pandas.core.frame.DataFrame df: 変換するDataFrame
    """
    df.to_csv("./ex4/output.tsv", sep="\t", index=True)


def read_tsv(path):
    """tsv形式のファイルを読み込む

    :param string path: TSVファイルのパス
    :return: TSVから読み込んだDataFrame
    """
    df = pd.read_csv(path, sep="\t")
    return df
