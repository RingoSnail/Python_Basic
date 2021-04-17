import pandas as pd
from pandas import Series, DataFrame

# 适合处理表格数据或异质数据
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)
print("-------------------")
obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
print(obj2)
print(obj2.values)
print(obj2.index)
print("-------------------")
print(obj2[obj2 > 0])  # 数学操作或过滤都会保留索引
print(obj2 * 2)
print("-------------------")
print(bool("e" in obj2))
print("-------------------")
data = {"Ohio": 35000, "Texas": 71000, "Oregon": 160000, "Utah": 50000}
obj3 = pd.Series(data)  # 字典转Series，按默认顺序索引
print(data)
print(obj3)
states = ["California", "Ohio", "Oregon", "Texas"]
obj4 = pd.Series(data, index=states)  # 可以指定索引顺序，但不改变对应关系
print(obj4)
print(obj4.isnull())  # 检查缺失数据
print("-------------------")
print(obj3 + obj4)  # 索引对齐
print("-------------------")
obj4.name = "population"
obj4.index.name = "state"
print(obj4)