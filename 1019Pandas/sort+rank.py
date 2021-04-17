import pandas as pd
import numpy as np

# 按索引排序
obj = pd.Series(range(4), index=["d", "a", "b", "c"])
print(obj.sort_index())  # 按索引排序

frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=["three", "one"],
                     columns=["d", "a", "b", "c"])
print(frame.sort_index())  # 按列索引排序
print(frame.sort_index(axis=1))  # 按行索引排序
frame.sort_index(axis=1, ascending=False)  # 按列索引降序排序
print("-----------------------------------")
# 按值排序
obj2 = pd.Series([4, np.NAN, 7, np.NAN, -3, 2])
print(obj2.sort_values())

frame2 = pd.DataFrame({"b":[4, 7, -3, 2], "a":[0, 1, 0, 1]})
print(frame2.sort_values(by="b"))
print(frame2.sort_values(by=["a", "b"]))
print("-----------------------------------")

# 排名
obj3 = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj3.sort_values())
print(obj3.rank())  # 按索引顺序显示，按数值给出排名
print(obj3.rank(method="first"))  # 靠前的排序靠前，不存在平均排名
print(obj3.rank(ascending=False, method="first"))

frame3 = pd.DataFrame({"b":[4.3, 7, -3, 2], "a":[0, 1, 0, 1],
                       "c":[-2, 5, 8, -2.5]})
print(frame3)
print(frame3.rank(axis="columns"))
print(frame3.rank())  # DataFrame也可按某一方向排名