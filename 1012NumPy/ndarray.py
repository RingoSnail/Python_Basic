import numpy as np

# ndarray：多维数组对象
data = np.random.randn(2, 3)
print("正态分布数组", data)

data = data * 100
print("数学操作", data)

data = data + data
print("数学操作", data)

print("属性", data.shape, data.dtype)

arr1 = np.array(data)
print(arr1, "维度", arr1.ndim)

z = np.zeros([3, 6])
print(z.T)
z2 = np.zeros((2, 3, 4, 5))
print("四维数组", z2)  # 两行三列个[4,5]矩阵
print(z2.shape)
print("------------------")

# 索引、切片
arr2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("切片", arr2[5:8])

arr2[5:8] = 12  # 并不是拷贝，而是视图,会直接修改到原数组
print("通过视图修改", arr2)

arr3 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("二维切片", arr3[1:, :2])
print("布尔索引", arr3[arr3 > 5])
print("------------------")

arr4 = np.random.randint(1, 10, size=(3, 5))
print(arr4)
print("矩阵行列数", arr4.shape)
print(arr4.shape[0])
print("矩阵的第三列", arr4.T[2])
