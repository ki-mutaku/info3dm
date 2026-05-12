import datasets
import regression

# %%

X, Y = datasets.load_linear_example1()
model = regression.LinearRegression()

# %%

print(model.x)
# print(X)
# print(X[0])
# print(Y)

# %%

model = regression.LinearRegression()
model.fit(X, Y)
print(model.theta)

# %%

print(model.predict(X))
print(model.score(X, Y))

# %%

X, Y = datasets.load_nonlinear_example1()
ex_X = datasets.polynomial2_features(X)
print(f"{ex_X=}")
print(f"{Y=}")

# %%

ex_X = datasets.polynomial3_features(X)
print(f"{ex_X=}")

# %%

model = regression.RidgeRegression(alpha=0.1)
model.fit(ex_X, Y)
print(f"{model.theta=}")

# %%
