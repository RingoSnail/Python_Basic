n = 100
while n > 0:
    n = n // 2
    print(n)
print("----------------")


def calc(n):
    n = n // 2
    print(n)
    if n > 0:
        calc(n)  # 调用自己


calc(100)
print("----------------")


def calc(n):
    n = n//2
    print(n)
    if n > 0:
        calc(n)
    print(n)  # 内层递归结束才进行此句


calc(10)
