import numpy as np

# (1) 5個の要素を持つ列ベクトル（値はすべて1）の作成
a = np.ones((5, 1))

# (2) 2番目の要素を3.14に変更
a[1, 0] = 3.14

# (3) 列ベクトルを複製
b = a.T

# (4) 列ベクトルと行ベクトルの内積
dot = np.dot(a, b)

# (5) np.random.rand()を使用して、10行1列のランダムな列ベクトルを作成
c = np.random.rand(10, 1)

# (6) np.random.normal()を使用して、正規分布の行列を作成
d = np.random.normal(loc=10, scale=2, size=(2,5))

# (7) dの２列目の要素を抜き出す
d_col2 = d[:, 1]

# (8) dの3,4列目の要素を抜き出す
d_col34 = d[:, 2:4]

# (9) np.random.randで5行2列の行列と、6で用意した行列との積
e = np.random.rand(5, 2)
de_dot = np.dot(d, e)

print(a)
print(b)
print(dot)
print(c)
print(d)
print(d_col2)
print(e)
print(de_dot)