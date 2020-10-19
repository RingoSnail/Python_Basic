name = "小猿圈"


def change():
    name = "小猿圈，自学编程"

    def change2():
        name = "小猿圈，自学编程不要钱"
        print("第3层打印", name)

    change2()
    print("第2层打印", name)


change()
print("第1层打印", name)
print("----------------")

res = map(lambda x: x ** 2, [1, 5, 7, 4, 8])  # 匿名函数,省去指定函数名的过程
for i in res:
    print(i)
print("----------------")


def get_abs(n):
    if n < 0:
        n = int(str(n).strip("-"))
    return n


def add(x, y, f):  # 低阶函数作为高阶函数的参数
    return f(x) + f(y)


res = add(3, -6, get_abs)
print(res)
