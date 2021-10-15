import re

formula = "1 - 2 * ((60 - 30 + (-9 - 2 - 5 - 2 * 3 - 5 / 3 - 40 * 4 / 2 - 3 / 5 + 6 * 3) * (-9 - 2 - 5 - 2 * 5 / 3 + " \
          "7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) /(16 - 3 * 2)) "

operators = re.findall("[\*\/]", formula)
calc_list = re.split("[\*\/]", formula)
plus_and_minus_operators = re.findall("[\+\-]", formula)
multiply_and_dividend = re.split("[\+\-]", formula)
n = re.findall(r"\([^()]+\)", formula)  # 找到独立的最内层的括号内容
m = re.findall(r"[\(\)]+", formula)  # 找到括号

print(operators)
print(calc_list)
print(plus_and_minus_operators)
print(multiply_and_dividend)
print(n)
print(m)
