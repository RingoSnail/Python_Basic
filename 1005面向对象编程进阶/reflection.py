class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("hi,guys , my name is ", self.name)


obj = Person('Alex', 26)

# 检测是否含有某属性
print(hasattr(obj, 'name'))
print(hasattr(obj, 'say_hi'))
# 获取属性
n = getattr(obj, 'name')
print(n)
func = getattr(obj, 'say_hi')
func()
# 设置属性
setattr(obj, 'hobby', "girl")
setattr(obj, 'show_name', lambda self: self.name + '--%s' % self.age)
print(obj.__dict__)
print(obj.show_name(obj))
# 删除属性
delattr(obj, 'age')
delattr(obj, 'show_name')

print(obj.__dict__)
