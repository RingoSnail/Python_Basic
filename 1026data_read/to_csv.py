import pandas as pd
import numpy as np
import sys

data = pd.read_csv("ex3")
data.to_csv("ex31")
data.to_csv(sys.stdout, na_rep="NULL", sep="|")  # 控制台打印，填补NaN值
data.to_csv(sys.stdout, index=False, header=False)
data.to_csv(sys.stdout, index=False, header=["v", "w", "x", "y", "z"], na_rep="NULL", sep="|")

dates = pd.date_range("1/1/2000", periods=7)
ts = pd.Series(np.arange(7), index=dates)  # 用日期做索引
ts.to_csv("tseries", header=False)