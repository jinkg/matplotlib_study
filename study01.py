import numpy as np
import pylab

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# pylab.plot(X, C)
# pylab.plot(X, S)
# 创建一个 8*6 点的图，分辨率为80
pylab.figure(figsize=(8, 6), dpi=90)
# 创建一个 1*1 点子图，接下来点图样绘制在其中点第 1 块
pylab.subplot(1, 1, 1)

pylab.plot(X, C, color='blue', linewidth=1.0, linestyle='--', label='cosine')
pylab.plot(X, S, color='green', linewidth=1.0, linestyle='-', label='sine')
# 添加图例
pylab.legend(loc='upper left')
# 横轴的上下限
pylab.xlim(-4.0, 4.0)

# 设置横轴记号
pylab.xticks(np.linspace(-4, 4, 9, endpoint=True))

pylab.ylim(-3, 3)
pylab.yticks(np.linspace(-1, 1, 5, endpoint=True))

pylab.show()
