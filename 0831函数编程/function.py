def calc(x, y):  # x,y 形参
    res = x ** y
    res2 = res * 2
    return res, res2


a, b = 2, 8  # a,b 实参
c = calc(a, b)
print(c)
print("----------------")


def stu_register(name, age, country, course="Python"):  # 默认参数
    print("----注册学生信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)


stu_register("王", 22, "CN", "python_devops")  # 位置参数，按顺序
stu_register("张", 21, "CN")
stu_register("刘", 25, "CN", "linux")
stu_register("李", 23, course="linux", country="CN")  # 用关键参数可不按顺序赋值
print("----------------")


# 非固定参数
def stu_register1(name, age, *args):  # *args 会把多传入的参数变成一个元组形式
    print(name, age, args)


stu_register1("Alex", 22)
stu_register1("Jack", 32, "CN", "Python")
print("----------------")


def stu_register2(name, age, *args, **kwargs):  # *kwargs 会把多传入的参数变成一个dict形式
    print(name, age, args, kwargs)


stu_register2("Alex", 22)
stu_register2("Jack", 32, "CN", "Python", sex="Male", province="ShanDong")
stu_register2("Jack", 32, sex="Male", province="ShanDong")
print("----------------")


def print_info(hobby="sleep", **kwargs):  # 将默认参数放在**kwargs前面
    print("info".center(20, "-"))
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("Sex:", kwargs["sex"])
    print("Hobby:", hobby)


print_info(name="Alex", age="22", sex="M")
print_info(name="Jack", age="26", sex="M", hobby="study")
print("----------------")

