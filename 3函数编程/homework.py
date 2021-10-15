func = lambda x, y: x + y  # 动态传参
print(func(1, 2))
print("----------------------")

file = open(file="namelist", mode="r", encoding="UTF-8")  # 读取并修改文件
a = []


def file_capital(file):
    for i in file:
        b = i.capitalize()
        b = b.strip()
        a.append(b)
    print(a)


def file_space(file):  # 数空格
    n = 0
    for i in file:
        i = str(i)
        for k in i:
            if k == " ":
                n += 1
    print("有%s个空" % n)


file_capital(file)  # 好像有冲突，以后再解决
# file_space(file)
print("----------------------")

dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}  # 截取2位字典元素


# 字典中的value只能是字符串或列表
def func(i):  # i为所传字典
    for k, v in i.items():
        if len(v) > 2:
            dic[k] = v[0:2]
        else:
            continue
    return i


print(func(dic))
print("----------------------")

poker_list = []
color = ["红心", "方片", "梅花", "黑桃"]
jqk = ["J", "Q", "K"]


def poker():
    for c in range(4):
        for n in range(13):
            if n >= 10:
                poker_list.append((color[c], jqk[n - 10]))
            else:
                poker_list.append((color[c], n + 1))
    poker_list.extend(["大王", "小王"])
    return poker_list


poker()
print(poker_list)
print("----------------------")


def maxmin():
    i = 0
    list_maxmin = []
    while i < 3:
        list_maxmin.append(input("传入"))
        i += 1
    else:
        print(f"max:{max(list_maxmin)},min:{min(list_maxmin)}")


maxmin()
