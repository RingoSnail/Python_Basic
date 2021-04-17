import pandas as pd
import numpy as np

# 与numpy相比，pandas可以处理缺失值
df = pd.DataFrame([[1.4, np.NAN], [7.1, -4.5],
                   [np.NAN, np.NAN], [0.75, -1.3]],
                  index=["a", "b", "c", "d"],
                  columns=["one", "two"])
obj = pd.Series(["a", "a", "b", "c"] * 4)

# 一些描述性统计和汇总统计
print(df)
print(df.sum())
print(df.sum(axis="columns"))  # NAN值会被自动排除
print(df.sum(axis="columns", skipna=False))  # 手动识别NAN值

print(df.idxmax())  # 返回每column的最大值的index
print(np.argmax(df["one"]))
print(df.cumsum())  # 累加每column
print(df.describe())  # 返回一些统计信息

print(obj)
print(obj.describe())
print(np.argmax(obj))
