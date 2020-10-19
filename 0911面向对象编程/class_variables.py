class Person:
    nationality = "Chinese"  # 全部人的国籍存一份就好，类属性和实例属性分开

    def __init__(self, name, sex, birthday, hometown):
        self.name = name
        self.sex = sex
        self.birthday = birthday
        self.hometown = hometown


p1 = Person("Alex", "Male", "1995-05-32", "山东德州")
p2 = Person("Jack", "Male", "1992-06-16", "河南信阳")
print(p1.nationality, p2.nationality)

p2.nationality = "Japan"  # 这个动作相当于把p2.nationality变成了实例变量
print(p1.nationality, p2.nationality)
