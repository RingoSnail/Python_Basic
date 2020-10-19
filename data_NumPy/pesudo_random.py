import numpy as np

s = np.random.normal(size=(5, 5))
print(s)
print("-------------")

S1 = np.random.RandomState(1234)
s1 = S1.randn(10)
print(s1)
print(np.random.permutation(s1))  # 随机排列
print("-------------")

print(np.random.rand(5, 3))  # 5行3列的[0-1）均匀分布样本
print(np.random.randn(5, 3))  # 0,1高斯分布
c_for_v_init = 2 + 0.5 * np.random.randn(6)
print(c_for_v_init)
