# 类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
class Student(object):
    stu_num = 0

    def __init__(self, name):
        self.name = name
        Student.stu_num += 1

    @staticmethod
    def fly(x):
        print("%s is flying..." % x.name)
        print(x.stu_num)


s = Student("Alex")
s.fly(s)  # 必须主动传参给静态方法
