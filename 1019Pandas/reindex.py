import pandas as pd
import numpy as np

obj = pd.Series([2.3, 2.4, -9.2, 3.1], index=["d", "c", "a", "b"])
print(obj)

obj2 = obj.reindex(["a", "b", "c", "d", "e"])  # 按索引重排列行
print(obj2)
print("------------------------------------------------------------")
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=["a", "c", "d"],
                     columns=["Ohio", "Texas", "California"])
print(frame)

frame2 = frame.reindex(["a", "b", "c", "d"],method="ffill")  # ffill即向前填充
print(frame2)

states = ["Texas", "Utah", "California"]
frame3 = frame.reindex(columns=states)
print(frame3)

frame4 = frame.reindex(index = ["a", "b", "c", "d"], columns = states)  # 行列全部重排序，且赋空值
print(frame4)