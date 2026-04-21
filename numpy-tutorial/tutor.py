import numpy as np

a = np.ones((5, 1))
a[1, 0] = 3.14

b = a.T

dot = np.dot(a, b)

c = np.random.rand(10, 1)

print(a)
print(b)
print(dot)
print(c)
