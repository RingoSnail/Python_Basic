# import os
# print(os.getcwd())
# print(os.listdir())
# data = open("ex1")
# print(data)
import pandas as pd

df = pd.read_csv("ex1")
print(df)

df2 = pd.read_table("ex1", sep=",")
print(df2)

# df3 = pd.read_csv("ex2")
# df3 = pd.read_csv("ex2", header=None)
df3 = pd.read_csv("ex2", names=["a", "b", "c", "d", "message"])  # 可以指定列名
print(df3)

df4 = pd.read_csv("ex2", names=["a", "b", "c", "d", "message"], index_col="message")  # 指定一列做索引
print(df4)


# na_values=0
# pd.options.display.max_rows = 10
# nrows
# chunksize