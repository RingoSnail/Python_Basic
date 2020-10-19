import os

f_name = input("要修改的文件：")
f_new_name = "%s_new" % f_name

old_str = input("要替换掉的文字：")
new_str = input("替换为：")

f = open(f_name, "r", encoding="UTF-8")
f_new = open(f_new_name, "w", encoding="UTF-8")  # 同时创建一个新文件
i = 0
for line in f:
    if old_str in line:
        new_line = line.replace(old_str, new_str)  # 全局查找替换 # 帮助文档说明replace会覆盖原文件
        i += 1
    else:
        new_line = line
    f_new.write(new_line)

f.close()
f_new.close()
print(f"替换了{i}处")
# os.rename(f_new_name,f_name)
# 把新文件名字改成原文件 的名字，就把之前的覆盖掉了,windows使用os.replace
