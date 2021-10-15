dict1 = {}
for i in range(1, 101):
    dict1[i] = i
print(dict1)

a = []
i = 0
while i <= 100:
    i += 1
    a.append(i)
    if i == 100:
        break
dict2 = {}.fromkeys(a, 0)
for k in dict2:
    dict2[k] = k
print(dict2)

dict3 = {"k0": 0, "k1": 1, "k2": 2, "k3": 3, "k4": 4, "k5": 5, "k6": 6}
for j in dict3:
    if dict3[j] > 5:
        print(dict3[j])

dict4 = {"k0": 0, "k1": 1, "k2": 2, "k3": 3, "k4": 4, "k5": 5, "k6": 6}
for j in dict4:
    if dict4[j]%2 == 0:
        dict4[j] = "-1"
        print(dict4)

dict5 = {'Ringo': ['Ringo', 25, 'researcher'],
         'Alex': ['Alex', 35, 'teacher'],
         'Jack': ['Jack', 56, 'boss'],
         }
name = str(input("请输入要查找的姓名："))
item = str(input("请输入要查找的项目："))
if item == "姓名":
    print(dict5[name][0])
elif item == "年龄":
    print(dict5[name][1])