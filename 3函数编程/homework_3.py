name = ["alex", "wupeiqi", "yuanhao", "nezha"]
name_sb = list(map(lambda x:x+"_sb", name))
print(name_sb)

num = [1,3,5,6,7,8]
num_even = list(filter(lambda x: x % 2 == 0, num))
print(num_even)