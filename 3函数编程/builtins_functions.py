print(ascii("中国"))
print(bin(10))
print(bool([]))  # 判断是否为空/0
print(all([1, 2, 3, 0]))  # 判断每个元素的bool是否都为true
print(any([1, 2, 3, 0]))  # 判断至少一个元素的bool为true
print(bytes("中国", "UTF-8"))
print(complex(10, 9))  # 生成复数
print(dir("a"))  # 返回对象的可调用属性(可调用的函数，方法) dir即directory
print("---------------------")

# names = ["Alex", "Jack"]
# f = open("eval_test", "w")
# f.write(str(names))

f = open("eval_test")
d = eval(f.read())  # 将现有str转换为原有的list格式
print(type(d))
print("---------------------")

exec("print('hello world')")  # 解释并执行字符串
print("---------------------")

l = list(filter(lambda x: x > 10, [1, 2, 3, 14, 15, 16]))  # 对可迭代对象进行过滤
print(l)

m = list(map(lambda x: x * 10, [1, 2, 3, 14, 15, 16]))  # 对可迭代对象进行计算
print(m)

print("---------------------")

print(globals(), "\n", locals())  # 打印出全局变量,局部变量
print("---------------------")

a = [1, 4, 9, 1849, 2025, 25, 36]
b = ["a", "b", "c", "d"]
print(list(zip(a, b)))  # 将两个列表拼成一个
print(dict(zip(a, b)))
print("---------------------")

print("a", "b", "c", "d", end="\n")