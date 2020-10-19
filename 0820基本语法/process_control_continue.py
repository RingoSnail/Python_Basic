count = 0

while count <= 100:  # 只要count<=100就不断执行下面的代码

    count += 1  # 每执行一次，就把count+1，要不然就变成死循环啦，因为count一直是0

    if 5 <= count <= 95:
        continue  # 只要count在5-95之间，就不走下面的语句，直接进入下一次loop
    if count % 2 == 0:
        print("loop ", count)

print("-----out of while loop ------")
