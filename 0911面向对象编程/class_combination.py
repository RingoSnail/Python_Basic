class Dog:

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = int(100)

    def bite(self, person):
        person.life_val -= self.attack_val
        print("狗[%s]咬了人[%s],人掉血[%s],还剩血量[%s]..." % (self.name, person.name, self.attack_val, person.life_val))


class Weapon:

    def stick(self, obj):
        """打狗棒"""
        self.name = "打狗棒"
        self.attack_val = int(40)
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def knife(self, obj):
        """屠龙刀"""
        self.name = "屠龙刀"
        self.attack_val = int(80)
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        """AK47"""
        self.name = "AK47"
        self.attack_val = int(100)
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print("[%s]被[%s]攻击了，掉血[%s],还剩血量[%s]..." % (obj.name, self.name, self.attack_val, obj.life_val))


class Person:
    role = 'person'

    def __init__(self, name, sex, attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = int(100)
        self.weapon = Weapon()  # 在此处实例化一个Weapon对象

    def attack(self, dog):
        dog.life_val -= self.attack_val
        print("人[%s]打了狗[%s],狗掉血[%s],还剩血量[%s]..." % (self.name, dog.name, self.attack_val, dog.life_val))


d = Dog("mjj", "二哈", 20)
p = Person("Alex", "Male", 60)
d.bite(p)  # 对象交互,把p实例传递给d的方法
p.attack(d)
p.weapon.knife(d)  # 通过组合的方式调用weapon实例下的具体武器
p.weapon.stick(d)
