a = ["alex", "eric", "rain"]
b = a[0] + a[1] + a[2]
print(b)
print("-------------------")

list1 = ["alec", " aric", "Alex", "Tony", "rain"]
tuple1 = ("alec", " aric", "Alex", "Tony", "rain")
dict1 = {'k1': "alec", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

for h, i in enumerate(list1, 0):  # enumerate函数  h for num(start:0), i for element.start是指定的下标，与list内的下标无关
    i = i.strip()
    list1[h] = i  # 修改list1
    if i.endswith("c") and i.startswith("a" or "A"):
        print(i)
print(list1)

for j in tuple1:
    j = j.strip()
    if j.endswith("c") and j.startswith("a" or "A"):
        print(j)
print(tuple1)

# for k in dict1:
#     dict1[k] = dict1[k].strip()  # 修改dict1
#     if dict1[k].endswith('c') and dict1[k].startswith("a" or "A"):
#         print(dict1[k])
# print(dict1)
# print("-------------------")

for l in dict1.values():
    l = l.strip()  # 不修改dict1
    if l.endswith('c') and l.startswith("a" or "A"):
        print(l)
print(dict1)
print("-------------------")

list2 = ["alec", " aric", "Alex", "Tony", "rain"]
print(len(list2))
print("-------------------")

list3 = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
list3[-1] = "ALL"
print(list3[2][1][1])
for m, n in enumerate(list3, 100):
    print(m, n)
print("-------------------")

tuple2 = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
tuple2[1][2]["k2"].insert(0, "Seven")
tuple2[1][2]["k3"] = [tuple2[1][2]["k3"], "Seven"]
print(tuple2)
print("-------------------")

s = "Alex"
print(list(s), tuple(s))

dict2 = dict(zip([i for i in range(10, len(list(s))+11)], list(s)))  # 列表转为字典
print(dict2)
print("-------------------")
