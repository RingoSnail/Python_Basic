count = 0
while count <= 5:
    count += 1
    if count == 3: break  # 如果执行过程中被break啦，就不会执行else的语句啦
    print("Loop", count)
else:
    print("循环正常执行完啦")
print("-----out of while loop ------")
