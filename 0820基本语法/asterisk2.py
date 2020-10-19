
n = int(input("请输入要打印的行数："))
i = 1
while i <= n:
    print("")
    if n % 2 == 1:
        j = (n + 1) / 2
    else:
        j = n/2 + 1
    if i <= j:
        k = 1
        while k <= i:
            print("*", end=" ")
            k += 1
    elif i > j:
        m = j - 1
        while m >= i - j:
            print("*", end=" ")
            m -= 1
    i += 1