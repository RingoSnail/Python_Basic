import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(4, 3),
                     index=["Utah", "Ohio", "Texas", "Oregon"],
                     columns=["b", "d", "e"])
print(frame)
print(np.abs(frame))

f = lambda x: x.max() - x.min()
print(frame.apply(f))  # 默认按行方向计算，即行增加的方向
print(frame.apply(f, axis="columns"))  # 指定按列增加的方向计算


def fx(x):
    return pd.Series([x.min(), x.max()], index=["min", "max"])


print(frame.apply(fx))

format = lambda x: "%.2f" % x  # 四舍五入取两位小数
print(frame.applymap(format))  # 对于DataFrame使用applymap方法
print(frame["e"].map(format))  # 对于Series用map方法


