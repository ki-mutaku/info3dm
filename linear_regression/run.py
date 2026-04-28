import datasets
import regression

X, Y = datasets.load_linear_example1()
model = regression.LinearRegression()

print(model.x)
# print(X)
# print(X[0])
# print(Y)
