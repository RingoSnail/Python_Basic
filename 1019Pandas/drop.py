import pandas as pd
import numpy as np

obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
print(obj)

new_obj = obj.drop("c")
print(new_obj)
print("-------------------------------------------")

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["One", "Two", "Three", "Four"])
print(data)

print(data.drop(["Colorado", "Ohio"]))
# data.drop(["Two", "Four"], axis=1, inplace=True)

data.drop(["Two", "Four"], axis="columns", inplace=True)  # inplace属性，对原对象直接操作
print(data)