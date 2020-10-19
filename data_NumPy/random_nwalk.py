import numpy as np
import matplotlib.pyplot as plt

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)  # 沿第二轴（横向）进行累加
print(walks)

hits30 = (np.abs(walks) >= 30).any(1)
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times.mean())
