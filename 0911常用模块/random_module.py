import random
import string

print(random.random())
print(random.randrange(1, 10))  # int型
print(random.choice("Ringo"))
print(random.sample("Ringo", 3))
print("-------------------")

print(" ".join(random.sample(string.ascii_lowercase + string.digits, 6)))  # 从小写字母和数字里随机选6个

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)
print(a)