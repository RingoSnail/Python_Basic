class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("Animal[%s] is eating..." % self.name)


class People(Animal):
    def __init__(self, name, age, sex, race):
        # Animal.__init__(self, name, age, sex)
        # super(People, self).__init__(name, age, sex)
        super().__init__(name, age, sex)  # 三种皆可，继承父类方法

        self.race = race  # 再加上子类的属性
        print("初始化了一个人....")

    def walk(self):
        print("People [%s] is walking..." % self.name)


p = People("Alex", "24", "male", "yellow")
p.walk()
p.eat()
