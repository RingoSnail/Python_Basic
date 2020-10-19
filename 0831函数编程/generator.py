for i in range(1000000):  # 浪费内存
    print(i)
    if i >= 100:
        break
print("---------------")

count = 0
while count <= 1000000:  # 不浪费内存
    print(count)
    count += 1
    if count > 100:
        break
print("---------------")

g = (x * x for x in range(1, 10))  # 只是把方法存到内存里，并未生成列表
print(next(g))
print("---------------")

for i in g:
    print(i)
