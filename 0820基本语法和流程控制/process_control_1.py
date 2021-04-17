count = 0

while count <= 2:  # 只要count<=100就不断执行下面的代码

    count += 1  # 每执行一次，就把count+1，要不然就变成死循环啦，因为count一直是0

    age_of_old_boy = int(input("请猜年龄:"))

    if age_of_old_boy == 50:
        print("恭喜猜对了！")
        break
    else:
        print("继续猜!")


print("-----out of while loop ------")