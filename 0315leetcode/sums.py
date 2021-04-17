def sums(x):  # 求数位和
    s = 0
    while x != 0:
        s += x % 10  # 取余
        x = x // 10  # 取10位
    return s