# 纯Python实现随机漫步
# import random
# import matplotlib.pyplot as plt
# position = 0
# steps = 1000
# walk = [position]
# for i in range(steps):
#     step = 1 if random.randint(0, 1) else -1
#     position += step
#     walk.append(position)
#
# plt.plot(walk[:1000])
# plt.show()

# NumPy实现随机漫步
import numpy as np
import matplotlib.pyplot as plt

steps = 1000
draws = np.random.randint(0, 2, size=steps)  # 直接一次性生成所有步进
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
print(walk.mean(), walk.min(), walk.max())

print((np.abs(walk) >= 10).argmax())  # 第一次到达+-10的步数

plt.plot(walk[:1000])
plt.show()
