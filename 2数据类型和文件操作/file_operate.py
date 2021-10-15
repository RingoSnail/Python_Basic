
# f = open(file=input("要读取的文件名："), mode="r", encoding="UTF-8")  # 只读模式  # 加上编码限制
# first_line = f.readline()
# data = f.read()
# print(first_line, "\n", data)
# print(f.mode)
# print("----------------")
#

# f = open(file=input("要读取的文件名："), mode="r", encoding="UTF-8")  # 循环文件
#
# for line in f:
#     line = line.split()
#     name,addr,height,weight,phone = line
#     height = int(height)
#     weight = int(weight)
#     if height > 170 and weight <= 50:
#         print(line)
# f.close()
# print("----------------")
#

# f = open(file=input("要读取的文件名："), mode="a", encoding="UTF-8")  # 追加模式
# f.write("\n 追加些什么")
# f.close()
# print("----------------")
#

# f = open(file="write.txt", mode="w", encoding="UTF-8")  # 创建模式
# f.write("创建操作")
# f.close()
# print("----------------")
#

f = open(file=input("要读取的文件名："), mode="r+", encoding="UTF-8")  # 读写模式
f.seek(172)  # 定位，否则会覆盖写到开头
f.write("{150}")  # 覆盖原位置内容
print(f.mode)
f.close()

