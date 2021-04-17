import pandas as pd
import numpy as np

# Series切片，Series相当于索引不止是整数的numpy array
obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
print(obj)
print(obj["b"])
print(obj[2])
print(obj[obj <= 2])
print(obj[0:3])  # 也不包含尾部
print(obj["a":"c"])  # abc都会切出来
# Series修改
obj["b":"c"] = 5
print(obj)
print("-----------------------------------")

# DataFrame索引
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["One", "Two", "Three", "Four"])
print(data)
print(data[["Three", "One"]])
print(data[:2])

print(data[data["Three"] > 5])
print(data < 5)  # 布尔索引
print("-----------------------------------")

# loc和iloc选择数据  分别严格基于标签和基于整数
print(data.loc["Colorado", ["Two", "Three"]])  # 单行多列选择
print(data.iloc[2, [3, 0, 1]])  # 利用整数标签iloc选择

print(data.iloc[[1, 2], [3, 0, 1]])
print(data.iloc[:, 1:3][data.Three > 5])  # 按列选择 234列，且Three列的值大于5的行
