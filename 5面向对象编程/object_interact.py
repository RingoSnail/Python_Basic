class Dog:
    role = "dog"

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self, person):
        person.life_val -= int(self.attack_val)
        print("狗[%s]咬了人[%s]，人掉血[%s]， 还剩血量[%s]。。"%(self.name, person.name, self.attack_val, person.life_val))


class Person:
    role = "person"

    def __init__(self, name, sex, attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = 100

    def beat(self, dog):
        dog.life_val -= int(self.attack_val)
        print("人[%s]打了狗[%s]，狗掉血[%s]， 还剩血量[%s]。。"%(self.name, dog.name, self.attack_val, dog.life_val))


d = Dog("毛毛", "二哈", "60")
p = Person("Alex", "男", "20")

d.bite(p)  # 对象交互
p.beat(d)
