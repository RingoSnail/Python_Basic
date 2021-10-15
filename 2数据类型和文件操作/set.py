ages = (11, 22, 33, 44, 55)
a = {1, 2, "2", "Ringo", ages}  # 集合只可以存不变类型，且去重，且自带排序

b = [1, 2, 3, 4, 2, 'alex', 3, 'rain', 'alex']
b = list(set(b))  # 列表去重
print(b)

c = set(b)
print(a & c, a | c, a - c, a ^ c)  # 集合运算 交集 并集 差集 对称差集（并集去除交集）
print(a.isdisjoint(c))  # 判断2个集合是不是不相交，返回True or False
print(a.issubset(c))  # 判断a是不是c的子集，返回True or False
print(a.issuperset(c))  # 判断a是不是c的父集，返回True or False

