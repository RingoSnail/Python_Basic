red = []
blue = []
count_red = 1
count_blue = 1

while count_red < 7:
    num = int(input("【%d】请选择红球号码：" % count_red))

    if not (0 < num <= 32):
        print("你选择的号码超出范围")
        continue
    if num in red:
        print("你选择的号码重复，请重新选择")
        continue
    # 正常执行
    else:
        count_red += 1
        red.append(num)

while count_blue < 3:
    num = int(input("【%d】请选择蓝球号码：" % count_blue))

    if not (0 < num <= 16):
        print("你选择的号码超出范围")
        continue
    if num in blue:
        print("你选择的号码重复，请重新选择")
    # 正常执行
    else:
        count_blue += 1
        blue.append(num)

print("你选择的红球有", red)
print("你选择的蓝球有", blue)
print("祝你中五百万！")
