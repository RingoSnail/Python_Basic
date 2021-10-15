count = -100

while count <= 100:  # 只要count<=100就不断执行下面的代码
    count += 1  # 每执行一次，就把count+1，要不然就变成死循环啦，因为count一直是0
    if count % 2 == 0:
        print("loop ", count)
    if count == 5:
        break



print("-----out of while loop ------")
