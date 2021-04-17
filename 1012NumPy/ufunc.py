import numpy as np

arr1 = np.array(range(10))

print("square", np.square(arr1))  # 通用函数 对每个元素都生效
print(arr1)

# arr2 = np.random.randint(0, 10, size=10)
arr2 = np.random.randint(0, 10, size=10)
print(arr2)

print(np.maximum(arr1, arr2))  # 通用函数 逐个比较最大值

arr3 = np.random.randn(5) * 10
print(arr3)

reminder, whole = np.modf(arr3)  # 返回一个浮点数的小数部分和整数部分
print(reminder, "\n", whole)

print(np.sqrt(arr3))
print(np.sqrt(np.abs(arr3)))
