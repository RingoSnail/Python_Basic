# a = [1, 2, 3, 4, 5]
# b = []
# for i in a:b.append(i+1)
# print(b)

# for index, i in enumerate(a):
#     a[index] += 1
# print(a)

# a = list(map(lambda x: x + 1, a))
# print(a)

a = [i+1 for i in range(5)]  # 列表生成式
print(a)
a = [i+1 for i in a]
print(a)