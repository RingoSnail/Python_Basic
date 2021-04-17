import pandas as pd
import numpy as np

obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])
uniques = obj.unique()
print(uniques)
print(obj.value_counts())

print(pd.value_counts(obj.values, sort=False))  #value_counts也是pandas的有效顶层方法

mask = obj.isin(["b", "c"])  # 属性过滤
print(mask)
print(obj[mask])

to_match = pd.Series(["c", "a", "b", "b", "c", "a"])
unique_vals = pd.Series(["c", "b", "a"])

print(pd.Index(unique_vals).get_indexer(to_match))  # get_indexer得到一个唯一值索引数组

data = pd.DataFrame({"QU1":[1, 3, 6, 3, 4],
                     "QU2":[2, 3, 1, 2, 3],
                     "QU3":[1, 5, 2, 8, 4]})
print(data)
result = data.apply(pd.value_counts).fillna(0)  # 统计不同数值在DataFrame里出现的次数
print(result)