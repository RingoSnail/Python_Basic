import numpy as np

arr1 = np.random.randint(0, 10, size=10)
arr2 = np.random.randint(10, 20, size=10)

np.savez("array", a=arr2, b=arr1)
n = np.load("array.npz")
print(n)
print(n["a"], "\n", n["b"])
