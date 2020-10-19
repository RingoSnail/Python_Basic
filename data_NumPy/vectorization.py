import numpy as np
import matplotlib.pyplot as plt

# 二维数组可视化
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show()
print("----------------")

# 条件逻辑操作数组
xarr = np.array(range(0, 10))
yarr = np.array(range(10, 20))
cond = np.array([True, False, True, False, True, False, True, False, True, False])
result = np.where(cond, xarr, "x")  # True赋值xarr,False赋值"x"
print(result)
print("----------------")

# 统计方法
arr1 = np.random.randint(-10, 10, size=[10, 10])
print(arr1.mean(), arr1.sum(), arr1.mean(axis=1))
print("----------------")

# 布尔方法
arr2 = np.random.randint(-10, 10, size=10)
arr3 = np.where(arr2 >= 0, True, False)
print(arr3, arr3.any(), arr3.all())
print("-----------------")

# 排序
arr4 = np.random.randn(5, 6)
print(arr4, "\n", "\n", np.sort(arr4, axis=1))

# 集合逻辑
arr5 = np.random.randint(0, 10, size=100)
print(np.unique(arr5))
print(any(np.in1d(arr5, [10])))
