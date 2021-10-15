staff_list = [
    ["Alex", 23, "CEO", 66000],
    ["黑姑娘", 24, "行政", 4000],
    ["佩奇", 26, "讲师", 40000],
]
for i in staff_list:
    if i[0] == '黑姑娘':
        print(i[-1])
        break

# ()元组 []列表 {}字典
info = {
    "name": "小猿圈",
    "mission": "帮一千万极客高效学编程",
    "website": "http://apeland.com"
}
print(info, info.keys(), info.values())  # dict{key:value}
print(info["name"])  # 取值

# 创建字典的方式
a = {"name": "Ringo", "age": 24}
a["job"] = "researcher"  # 增加

b = dict(Ringo=["Ringo", 24, "researcher"], Alex=["Alex", 35, "teacher"])
b["Jack"] = ["Jack", 50, "merchant"]  # 增加或修改
b["Ringo"] = ["Ringo", 25, "researcher"]
b.setdefault("Oldboy", ["Oldboy", 56, "boss", 10000])  # 增加，且不能修改
del b["Jack"]  # 删除key
b.update(a)  # 合并字典

n = [1, 2, 3, 4, 5]
c = {}.fromkeys(n, 100)

print(a, "\n", b, "\n", c)
print(b["Ringo"])
print(b.keys(), b.values(), b.items())

for i in b:
    print(i, b[i])

print(len(b))  # 查询字典长度