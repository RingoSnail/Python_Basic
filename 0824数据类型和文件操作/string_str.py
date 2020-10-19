name = "Alex"
print(name[0], name[1:3], name[::-1])  # 字符串就相当于一个列表，也可取值，但不可修改
name = r"Alex\n"  # r即raw，原生字符
print(name)

names = "Ringo"
print(names.capitalize())  # 开头大写
print(names.casefold())  # 全部小写
print(names.lower())  # 全部小写
print(names.upper())  # 全部大写
print(names.swapcase())  # 大小写交换
print(names.center(50, "-"))  # 装饰线
print(names.count("r", 0, 4))  # 计数
print(bool(names.endswith("go")))  # 判断结尾
print(names.find("i"))  # 返回下标
print(names.index("go"))  # 返回字符串下标
print(bool(names.isdigit()))  # 判断是否全为数字
print(bool(names.islower()))  # 判断是否全为小写

say = "My name is {0}, I‘m {1} years old.{0} is my English name."  # {}表示占位，且可以反复引用
print(say.format(names, 24))  # 格式输出
print(f"My name is {names}, I'm 24 years old.{names} is my English name.")

n = ["alex", "jack", "rain"]
print("|".join(n))  # 插入间隔符
print(names.ljust(10, "|"))  # 从左数起，填充

namess = "\t    Ri ngo    \n    "
print(namess.strip())  # 只取出字符串 去除空格，换行符

score = "My score is 600, 600 is not very good."
print(score.replace("600", "700", 1))  # 替换字符串，计次数

names2 = "Alex,Jack,Rain"  # 分割字符串变成列表，用,分
print(names2.split(","), names2.split(",", 1))

print(bool(names2.startswith("a")))  #判断开头