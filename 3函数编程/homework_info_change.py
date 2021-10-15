dic = {"username": ["password", "age", "position", "department", "phone"],
       "alex": ["abc123", 30, "Engineer", "IT", 13651830433],
       "rain": ["df2@432", 25, "Teacher", "Teaching", 18912334223],
       "黑姑娘": ["df2@432", 26, "行政", "人事", 13811177306]
       }
info = """1. 打印个人信息
2. 修改个人信息
3. 修改密码
"""


def opt_1(name):
    info_1 = """Name:   %s
Age :   %s
Job :   %s
Dept:   %s
Phone:  %s
""" % (name, dic[name][1], dic[name][2], dic[name][3], dic[name][4])
    print(info_1)


def start(count=0):
    while count <= 2:
        name = str(input("请输入用户名："))
        password = str(input("请输入密码："))
        if name in dic.keys() and password == dic[name][0]:
            print("-----登陆成功，选择操作-----")
            operate = input(info)
            if operate == str(1):
                opt_1(name)
        else:
            print("错误")
            count += 1
    else:
        print("退出")


start()
