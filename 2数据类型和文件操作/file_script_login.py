print("———————登陆程序———————")

i = 0
while i <= 5:
    account = str(input("账号："))
    key = str(input("密码："))

    if i >= 3 and account == "Ringo" and key == "pop":
        print("虽然对了，但今日次数用尽")
        break

    elif account == "Ringo" and key == "pop":
        f = open("login_script", mode="w", encoding="UTF-8")
        f.write(f"账号:{account} \n")
        f.write(f"密码:{key}")
        break
    else:
        print("账号或密码错误")
        i += 1
print("今日次数用尽")
