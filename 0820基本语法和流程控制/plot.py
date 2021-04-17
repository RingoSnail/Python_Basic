import matplotlib.pyplot as plt  # 图库 #号注释且空两格
import numpy as np  # 随机数
import math

x = np.arange(0, math.pi, 0.001)  # np.arange(start,stop,step)
y = np.sin(x)

plt.plot(x, y)
plt.grid()  # 加网格
plt.show()
print(math.pi)
