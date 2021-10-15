# 写一个程序，要求用户输入用户名和密码，要求密码长度不少于6个字符，且必须以字母开头，
# 如果密码合法，则将该密码使用md5算法加密后的十六进制概要值存入名为password.txt的文件，超过三次不合法则退出程序
def start():
    count = 3
    while count > 0:
        name = input(">>").strip()
        pwd = input(">>").strip()
        if len(pwd) >= 6 and pwd[0].isalpha():
            pwd_md5 = hashlib.md5(pwd.encode("utf-8")).hexdigest()
            print("输入成功")
            obj = {"user_name:",  name, "pass_word:", pwd_md5}
            with open("password.txt", "a", encoding="utf-8") as f:
                json.dump(list(obj), f)
            exit()
        else:
            if count == 0:
                print("三次错误")
                exit()
            count -= 1
            print(f"输入错误，还有{count}次机会")
            continue


if __name__ == '__main__':
    import hashlib, json
    start()