import pandas as pd
from pandas import Series, DataFrame

# DataFrame就是一种有索引的字典，
# 或者二维Series（好几个Series并列，共用一套index，Series的名字是columns）
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2000, 2001, 2002],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print("----------------------")
# 指定行列标签
frame2 = pd.DataFrame(data, columns=["year", "pop", "state", "debt"],
                      index=["one", "two", "three", "four", "five", "six"])
print(frame2)
print(frame2.columns)
print(frame2["state"])  # 按列选取，自动输出Series
print(frame2.loc["three"])  # 行选取使用loc，iloc方法
print("----------------------")
frame2["debt"] = range(6)  # 创建新列
print(frame2)
val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "six"])
frame2["debt"] = val
print(frame2)
frame2["eastern"] = frame2["state"] == "Ohio"
print(frame2)
del frame2["eastern"]
print(frame2.columns)
print("----------------------")
# 嵌套型字典生成DataFrame，内部键成为索引
pop = {"Nevada": {2001: 2.4, 2002: 2.9},
       "Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.T)
print(pd.DataFrame(pop, index=[2000, 2001, 2002, 2003]))  # 显式指定索引
print(frame3.index.name)
print(frame3.columns.name)
print(frame3.columns)
print(frame3.values)
