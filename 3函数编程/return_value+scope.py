def stu_register(name, age, course='PY', country='CN'):
    print("----注册学生信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)
    if age > 22:
        return False  # 设置返回值
    else:
        return True


registration_status = stu_register("王山炮", 22, course="PY全栈开发", country='JP')
if registration_status:
    print("注册成功")
else:
    print("too old to be a student.")
print("----------------")

name = "Alex"  # 声明一个全局变量


def change_name():
    global name  # 声明一个全局变量，即可函数内修改全局变量，否则只是在函数内修改局部变量
    name = "金角大王"
    print("after change", name)


change_name()
print("在外面看看name改了么?", name)
