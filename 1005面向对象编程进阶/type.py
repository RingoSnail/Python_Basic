def __init__(self, name, age):
    self.name = name
    self.age = age
    print("init. ", name, age)


Person = type("Person", (object,), {"__init__": __init__})  # 用type动态地生成类
# Person 第一参数是类名
# (object,) 是这个类要继承的类
# {"__init__":__init__}是这个类的方法
p = Person("Alex", 22)
print(type(p))  # p对象是Person类的一个实例
print(type(Person))  # Person类对象是 type 类的一个实例

