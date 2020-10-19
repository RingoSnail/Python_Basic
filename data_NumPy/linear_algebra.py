import numpy as np
import numpy.linalg


np.set_printoptions(precision=3, suppress=True)  # 控制小数点位数

# 矩阵乘法
x = np.array([[1, 2, 3], [1, 2, 3]])
y = np.array([[10, 0], [10, 0], [10, 0]])
z = np.dot(x, y)
# z = x @ y
# z = x.dot(y)
print(z)
print("-----------------")

# 逆矩阵
X = np.random.randn(5, 5)
mat = X.T.dot(X)
print(numpy.linalg.inv(mat))  # 求mat的逆矩阵
print(mat.dot(numpy.linalg.inv(mat)))  # 得出单位矩阵
print("-----------------")

# 矩阵分解
q, r = numpy.linalg.qr(mat)  # Q,R矩阵
print(q, "\n", r)
print("-----------------")

print(numpy.linalg.svd(mat))