a = 2
b = 9

c = a + b
c = a - b
c = a * b
c = a ** b
c = b / a
c = b % a  # 模运算
c = b // a  # 整除 取商的整数部分
b += a  # 赋值运算
b **= a

print(a, b, c)

print(bool(not a <= b))  # 逻辑运算符

print(bool(a >=2 and b >= 2))

print(divmod(5, 2))  # 返回整除的商和余数

print(round(10.15, 1))  # 四舍五入，位数
