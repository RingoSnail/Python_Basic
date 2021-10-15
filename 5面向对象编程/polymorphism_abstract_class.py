# 通过抽象类实现多态(最常用)
class Document:  # 定义一种抽象类来实现多态
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")  # 主动报错，子类必须重写抽象方法show()


class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'


class Word(Document):
    def show(self):
        return 'Show word contents!'


documents = [Pdf('Document1'),
             Pdf('Document2'),
             Word('Document3')]
for document in documents:
    print(document.show() + ': ' + document.name)

print("----------------------------------------------------")


class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class SportsCar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar braking!'


class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'


cars = [Truck('东风重卡'),
        Truck('三一重工'),
        SportsCar('Tesla Roadster')]
for car in cars:
    print(car.name + ":" + car.drive())
    print(car.name + ":" + car.stop())
