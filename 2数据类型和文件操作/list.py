names = ["alex", "jack", "eva"]
names.append("ringo")  # 追加
names.insert(2, "black")  # 插入
names.insert(0, [1, 2, 3])  # 嵌套
names2 = ["egg", "chicken"]
names.extend(names2)  # 合并
print(names)
print(names[0][0])  # 嵌套情况输出

del names[0:3]  # 删除
names.pop(-1)  # 删除并输出
names2.clear()  # 清空
print(names)

names[0] = "金角大王"  # 修改元素
i = names.index("ringo")  # 查索引
c = names.count("ringo")  # 查个数
print(names, i, c)

print(names[1:4], names[-3:])  # 切片 最后一个值不取出来

print(names[0:5:2])  # 步长取值
print(names[::-1])  # -1步长取值可以反转列表

names.sort()  # 排序
names.reverse()  # 反转
print(names)

for a in names:
    print(a)  # 循环输出列表

size = 20
path_list = list(range(size + 2))  # 初始化路径
print(path_list)


