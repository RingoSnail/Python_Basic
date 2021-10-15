class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("animal:eat")


class Person(Animal):  # 继承

    def eat(self):
        print("person:eat")  # 重构父类的方法


p = Person("Alex", "24", "Male")

print(p.name)
p.eat()
