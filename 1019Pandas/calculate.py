import pandas as pd
import numpy as np

# Series算术运算
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])
print(s1 + s2)
print("----------------------------")

# DataFrame算术运算
df1 = pd.DataFrame(np.arange(9.).reshape(3,3),
                   columns=[list("bcd")],
                   index=["Ohio", "Texas", "Colorado"])
df2 = pd.DataFrame(np.arange(12.).reshape(4,3),
                   columns=[list("bde")],
                   index=["Utah", "Ohio", "Texas", "Oregon"])
print(df1 + df2)  # 索引，列会自动求并
print("----------------------------")

# 使用填充值
df3 = pd.DataFrame(np.arange(12.).reshape(3,4),
                   columns=[list("abcd")])
df4 = pd.DataFrame(np.arange(20.).reshape(4,5),
                   columns=[list("abcde")])
print(df3 + df4)
print(df3.add(df4, fill_value=0))
print("----------------------------")

# 算数方法副本 df1。rdiv(1) 相当于 1/df1
print(1/df1)
print(df1.rdiv(1))
print("----------------------------")

# DataFrame与Series间的算术: 广播机制
arr = np.arange(12.).reshape(3, 4)
print(arr)
print(arr - arr[0])
print("----------------------------")

frame = pd.DataFrame(np.arange(12.).reshape(4, 3),
                     columns=[list("bde")],
                     index=["Utah", "Ohio", "Texas", "Oregon"])
print(frame)
series = frame.iloc[0]
series2 = pd.Series(range(3), index=[list("bef")])
series3 = frame.iloc[:, 1]

print("减去第一行的广播", "\n", frame - series)
print("加上索引不同的一行的广播", "\n", frame + series2)
print("减去第二列的广播", "\n", frame.sub(series3, axis=0))
# axis="index" 列上广播，行上匹配    
