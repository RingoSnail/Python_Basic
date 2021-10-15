name = "Ringo"
age = 24
height = None

a = bool(type(name) is str)
b = bool(name is age)  # 身份运算
print(name, age, height, a, b)
