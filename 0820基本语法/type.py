a = "2**66"
b = 2 ** 60
c = 2.06
msg = """
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。"""
names = "Alex,Jack,Rain,Rachel,Mack..."
names = ["Alex", "Jack", "Rain", "Rachel", "Mack"]  # 列表
print(type(a), a, "\n", type(b), b, "\n", type(c), c, "\n", type(msg), msg, "\n", bool(c > b), "\n", type(names), names, names[2])

print(id(a))

a = 2
print(id(a))
