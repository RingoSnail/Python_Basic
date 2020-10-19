deposit = 10000
interest = 0.0325
count = 0

while count < 100:
    count += 1
    deposit *= (1+interest)
    if deposit >= 20000:
        break

print(f"第{count}年时翻番")