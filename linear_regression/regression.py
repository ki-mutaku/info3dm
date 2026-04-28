import numpy as np


class LinearRegression:
    x = None
    theta = None
    y = None

    def fit(self, x, y):
        """
        >>> import regression, datasets
        >>> X,Y = datasets.load_linear_example1()
        >>> model = regression.LinearRegression()
        >>> model.fit(X, Y)
        >>> model.theta
        array([5.30412371, 0.49484536])
        """
        temp = np.linalg.inv(np.dot(x.T, x))
        self.theta = np.dot(np.dot(temp, x.T), y)

    def predict(self, x):
        """
        >>> import regression, datasets
        >>> X,Y = datasets.load_linear_example1()
        >>> model = regression.LinearRegression()
        >>> model.fit(X, Y)
        >>> print(model.predict(X))
        [ 7.28350515  9.2628866  11.7371134  13.71649485]
        """
        return np.dot(x, self.theta)

    def score(self, x, y):
        pass
