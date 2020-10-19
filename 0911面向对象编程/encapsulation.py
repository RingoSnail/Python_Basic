# 私有变量和私有方法
# 在python中用双下划线开头的方式将属性隐藏起来（设置成私有的）
class A:
    M = 0
    __N = 1  # 类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N

    def __init__(self):
        self.__X = 10  # 变形为self._A__X
        print("初始化")

    def __foo(self):  # 变形为_A__foo
        print('from A')

    def bar(self):
        self.__foo()  # 只有在类内部才可以通过__foo的形式访问到.


a = A()
print(a.M)
print(a._A__N)  # A._A__N是可以访问到的，即这种操作并不是严格意义上的限制外部访问，仅仅只是一种语法意义上的变形
print(a._A__X)  # 强行访问实例的私有变量
a._A__foo()  # 强行使用私有方法
a.bar()

