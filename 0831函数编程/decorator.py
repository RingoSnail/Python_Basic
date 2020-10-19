account = {
    "is_authenticated": False,  # 用户登录了就把这个改成True
    "username": "alex",  # 假装这是DB里存的用户信息
    "password": "abc123"  # 假装这是DB里存的用户信息
}


def login(func):
    def inner(*args, **kwargs):  # 不定参数，为传给func准备的
        if account["is_authenticated"] is False:
            username = input("user:")
            password = input("password:")
            if username == account["username"] and password == account["password"]:
                print("welcome login....")
                account["is_authenticated"] = True
                func(*args, **kwargs)  # 认证成功，执行功能函数，即几个页面
            else:
                print("wrong username or password!")
        else:
            print("用户已登录，验证通过...")
            func(*args, **kwargs)  # 认证成功，执行功能函数

    return inner  # 闭包


def home():
    print("---首页----")


@login  # 装饰器: 相当于america = login(america)
def america():
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


@login
def henan(vip_level):  # 甚至可以往里传参
    if vip_level < 3:
        print("----河南专区普通会员----")
    else:
        print("欢迎来到尊贵河南口音RMB玩家私密社区".center(50,"-"))
        print("再充值500就可以获取演员微信号，幸福大门即将开启".center(50," "))


home()
america()
japan()
henan(5)
