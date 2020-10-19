# 通过统一函数接口实现多态
class Dog(object):
    def sound(self):
        print("汪汪汪.....")


class Cat(object):
    def sound(self):
        print("喵喵喵.....")


def make_sound(x):
    """统一调用接口"""
    x.sound()  # 不管你传进来是什么动物，我都调用sound()方法


d = Dog()
c = Cat()
make_sound(d)
make_sound(c)