import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
n = 50
X = np.random.normal(0, 1, n)
# Y = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.random.normal(0, 1, n)
colors = np.random.randn(n)
# area = np.pi * (15 * np.random.randn(n)) ** 2
area = 30


# plt.scatter(X, Y)
# plt.scatter(X, Y, s=area, c=colors, alpha=0.5)

def f(x, y):
    # return x + 2 * y
    return x == y


n = 3
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

# plt.contourf(X, Y, f(X, Y), 1, cmap=plt.cm.Spectral)
# plt.contourf(X, Y, f(X, Y))
# Z = np.array([[1, 1, 1, 0.5], [1, 1, 0.5, 0.1], [1, 0.5, 0.1, 0.1], [0.5, 0.1, 0.1, 0.1]])
# Z = np.array([[1, 2, 3, 4], [2, 3, 4, 3], [3, 4, 3, 2], [4, 3, 2, 1]])
Z = f(X, Y)
plt.contourf(X, Y, Z)
plt.show()


def plot_decision_boundary(model, X, y):
    # Set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[0, :], X[1, :], c=y, cmap=plt.cm.Spectral)
    plt.show()
