import pandas as pd
import numpy as np

# 重复的索引是允许存在的
obj = pd.Series(range(5), index=["a", "a", "b", "b", "c"])
print(obj.index.is_unique)
print(obj)
print(obj["a"])
print(obj["c"])

frame = pd.DataFrame(np.random.rand(5, 3),
                     index=["a", "a", "b", "b", "c"])
print(frame)
print(frame.loc["a"])
print(frame.loc["b"])
print(frame.loc["c"])