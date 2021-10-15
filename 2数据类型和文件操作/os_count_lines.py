import os
import re

a = os.listdir("C:/Users/Ringo/PycharmProjects/Hi_python/2数据类型和文件操作")
a.remove(a[-1])
print(a)

for root in a:
    fh = open(root, 'r', encoding='utf-8')
    read_fh = fh.readlines()
    fh.close()
    number_code = 0
    number_empty = 0
    number_note = 0
    pattern = '.*#'  # 正则匹配模式

    for x in read_fh:
        if '#' in x:  # 计算注释数目
            if re.findall(pattern, x)[0][:-1].isspace() or re.findall(pattern, x)[0][:-1] == '':
                number_note += 1
            else:
                number_code += 1
        elif x.isspace():  # 计算空行数  # 最后的一行空行最好都不要打
            number_empty += 1
        else:
            number_code += 1
    print(root.center(30, "-"))
    print('code number is %d' % (number_code + number_empty + number_note))
    print('empty number is %d' % number_empty)
    print('note number is %d' % number_note)
