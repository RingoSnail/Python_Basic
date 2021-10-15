height = 100
DECREASE = 0.5
length = 0
count = 0

while height >= 0:
    count += 1
    length = length + (height * (1 + DECREASE))
    height *= DECREASE

    if count == 10:
        print(f"第{count}次弹起的高度为{height},路程为{length}")
        break
