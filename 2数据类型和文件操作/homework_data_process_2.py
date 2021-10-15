lis = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic = {"k1": [], "k2": []}
list1 = []
list2 = []
for i in lis:
    if int(i) > 66:
        dic["k2"].append(i)
    else:
        dic["k1"].append(i)
print(dic)
print("-------------------")

li = [1, 3, 2, 7, 6, 23, 41, 243, 33, 85, 56]
a = li[0]
for i in li:
    if i > a:
        a = i
    else:
        continue
print(a)
print("------------------")

