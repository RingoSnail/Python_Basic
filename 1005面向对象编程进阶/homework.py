def __init__(self, name):
    self.name = name


def talk(self):
    print(f"Person {self.name} talk")


Person = type("Person", (object,), {"__init__": __init__, "talk": talk})

p = Person("Alex")
p.talk()
print("--------------------------------------")


class OverException(BaseException):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


def calc():

    x = int(input("第一个数："))
    y = int(input("第二个数："))

    try:
        if x + y >= 10:
            raise OverException("错误：超出范围")

    # except OverException as o:
    #     print(o)
    except Exception as e:
        print(e)
    else:
        print(x + y)


calc()


