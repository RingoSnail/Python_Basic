# 类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
class Dog(object):
    name = "class_variable_name"

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(cls):
        print("%s is eating" % cls.name)  # 只能访问类变量name，而不是实例变量name


d = Dog("Alex")
d.eat()
print("--------------------------------")


class Student(object):
    # 封装成私有变量
    __stu_num = 0  # 学员计数需存在类变量里，不能存在每个实例里，因为每个实例的内存是独立的，每实例化一次，数据就会被重置一次，不会累加

    def __init__(self, name):
        self.name = name
        self.add_stu_num()

    @classmethod
    def add_stu_num(cls):  # 注意这里调用时传进来的其实是类本身，不是实例本身，所以参数名一般改为cls
        cls.__stu_num += 1
        print("total student num:", cls.__stu_num)


s1 = Student("张1")
s2 = Student("张2")
s3 = Student("张3")
s4 = Student("张4")
