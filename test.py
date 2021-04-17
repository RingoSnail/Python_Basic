import random
import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

cost = [30, 40, 50, 100, 200, 400]

delay = [8.778807537, 6.828015, 6.56922, 1.9157, 1.53802, 1.384085]
for i in range(len(delay)):
    delay[i] = delay[i] * 13 / 60

# throughput = [0.068829, 0.037998, 0.03614457, 0.00185, 0.00185, 0.00185]
# for i in range(len(throughput)):
#     throughput[i] = 1 - throughput[i]

matplotlib.rcParams["legend.handlelength"] = 1
matplotlib.rcParams['legend.handleheight'] = 1

# plt.title('显示中文标题')
plt.xlabel("Cost Budget")
plt.ylabel("Average Delay(minutes)")
# plt.ylabel("Throughput Percentage")

plt.xlim((30, 400))
plt.ylim((0, 2))

plt.scatter(cost, delay, s=4)  # 散点
plt.plot(cost, delay, linewidth=1, label="improved greedy")  # 线  是label不是lable

plt.savefig(f'C:/Users/Ringo/PycharmProjects/RSU/versus_cost.png', dpi=750, bbox_inches='tight')
plt.clf()
plt.show()