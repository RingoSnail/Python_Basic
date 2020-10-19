import numpy as np
import time

# NumPy适合处理大量数组数据
l1 = list(range(1000000))
l2 = np.arange(1000000)

start_CPU = time.time()
for _ in range(7): l1 = l1 * 2
end_CPU = time.time()
print("list方法: %f CPU seconds" % (end_CPU - start_CPU))

start_CPU = time.time()
for _ in range(7): l2 = l2 * 2
end_CPU = time.time()
print("NumPy方法: %f CPU seconds" % (end_CPU - start_CPU))
