a = {"name": "Ringo", "age": 24}
d = a["name"]  # hash
print(d)
print(hash(a["name"]), hash(d))

print(0xA1, 0b1010, 0o73)  # 进制

s = "小猿圈"
print(s)
print(s.encode("utf-8"))  # 以utf-8编码 一个汉字3个字节
