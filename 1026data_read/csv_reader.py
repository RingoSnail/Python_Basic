# 逗号分隔值（Comma-Separated Values，CSV
# 有时也称为字符分隔值，因为分隔字符也可以不是逗号）
# 其文件以纯文本形式存储表格数据（数字和文本）
import csv

# f = open("ex4")
# reader = csv.reader(f)
# for line in reader:
#     print(line)

# csv模块读取csv文件
with open("ex4") as f:
    lines = list(csv.reader(f))

# 变成字典
header, values = lines[0], lines[1:]  # 第一行变成列名
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)


# 自定义一个csv.Dialect来自定义风格
class my_dialect(csv.Dialect):  # 自定义一个csv.Dialect来自定义风格
    lineterminator = "\n"  # 行终止符
    delimiter = ";"  # 字段分隔符
    quotechar = '"'  # 引号
    quoting = csv.QUOTE_MINIMAL  # 引用惯例


reader = csv.reader(lines, my_dialect)

# 写入csv文件
with open("mydata", "w") as m:
    writter = csv.writer(m, dialect=my_dialect)
    writter.writerow(("one", "two", "three"))
    writter.writerow(("1", "2", "3"))