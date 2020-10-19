dict1 = {
    "name":"alex",
    "age":18,
    "scores":{
        "语文":130,
        "数学":60,
        "英语":98,
    }
}
dict2 = dict1
dict3 = dict1.copy()

dict1["age"] = 20
dict1["scores"]["数学"] = 77  # 浅copy 只有第一层独立

print(dict1)
print(dict2)
print(dict3)

list1 = [10, 20, 30]
list2 = list1
list1[0] = 11
print(list2)