# 循环取余
def reminder(x, a, p):
    rem = 1  # x^1也没问题
    for _ in range(a):
        rem = (rem * x) % p
    return rem
# 快速幂取余
def reminder(x, a, p):
    rem = 1
    while a > 0:
        if a%2: rem = (rem * x) % p  # 幂是奇数时，转化一下，这时余数rem会变化
        x = x ** 2 % p  # 幂是偶数时，x和a变换后余数rem不变
        a = a // 2
    return rem