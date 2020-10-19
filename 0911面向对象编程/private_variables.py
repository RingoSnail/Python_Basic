class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__life_val = int(100)

    def got_attack(self):
        self.__life_val -= int(20)
        print(self.__life_val)


p = Person("Alex", "24")
p.got_attack()

p._Person__life_val -= int(20)  # 知道类名和私有变量名才可强行修改私有变量
print(p._Person__life_val)
