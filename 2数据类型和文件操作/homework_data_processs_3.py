li = [-100, 1, 3, 2, 7, 6, 120, 121, 140, 23, 411, 99, 243, 33, 85, 56]
# a = li[0]
# b = li[0]
# for i in li:
#     if i > a:
#         a = i
#     elif i < b:
#         b = i
#     else:
#         continue
c = (max(li) + min(li)) / 2
li2 = [abs(k - c) for k in li]
print(li[li2.index(min(li2))])
print("----------------------")

for i in range(1, 10):  # 九九乘法表
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}",end=" ")  # end=" "即此句print不换行，以空格结尾
    print(" ")  # 循环完j再换行
print("----------------------")

sum = 0
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # 不能被小于自己的任一数整除
        sum = sum + i
        print(i)
print(sum)
print("----------------------")

