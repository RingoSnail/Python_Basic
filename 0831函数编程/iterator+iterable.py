from typing import Iterable, Iterator

print(isinstance((x ** 2 for x in range(10)), Iterable))  # 可迭代对象
print(isinstance((x ** 2 for x in range(10)), Iterator))  # 迭代器

print(isinstance(iter([]), Iterable))
print(isinstance(iter([]), Iterator))  # iter()转为迭代器
