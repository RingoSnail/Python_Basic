class Dog(object):  # 类名首字母要大写，驼峰体
    d_type = "京巴"  # 公共属性，又称类变量，存在类的内存里

    def __init__(self, name, age, master):  # 初始化函数，只要一实例化，就会自动执行
        print("初始化这个实例。。", name)
        self.name = name  # self接收了实例的内存地址，把变量存在实例的内存里
        self.sge = age
        self.master = master

    def say_hi(self):  # 类的方法，必须带一个self参数，代表实例本身
        print("hallo, I am a dog, my type is", self.d_type, "my name is", self.name)


d1 = Dog("毛毛", "2", "Alex")  # 生成实例
d2 = Dog("二狗", "3", "Jack")

d1.say_hi()
d2.say_hi()

print(id(d1.d_type))
print(id(d2.d_type))
print(d2.name)
print(Dog.d_type)
print(Dog.say_hi)
