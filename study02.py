import numpy as np
import pylab

np.random.seed(1)
n = 50
X = np.random.normal(0, 1, n)
# Y = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.random.normal(0, 1, n)
colors = np.random.randn(n)
# area = np.pi * (15 * np.random.randn(n)) ** 2
area = 30
# pylab.scatter(X, Y)
pylab.scatter(X, Y, s=area, c=colors, alpha=0.5)
pylab.show()
