import random


class Student(object):
    stu_num = 0

    def __init__(self, name):
        self.name = name

    @property
    def fly(self):
        print("%s is flying..." % self.name)


s = Student("Alex")
s.fly  # fly此时已经变成一个静态属性了， 不是方法了
print("---------------------------")


class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("connecting airline company api... ")
        print("checking flight %s status..." % self.flight_name)
        return random.randint(0, 3)

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got canceled")
        elif status == 1:
            print("flight is arrived")
        elif status == 2:
            print("flight has departed already")
        else:
            print("cannot confirm the flight status,please check later")

    @flight_status.setter  # 修改
    def flight_status(self, status):
        status_dic = {
            0: "canceled",
            1: "arrived",
            2: "departed"
        }
        print("\033[31;1mHas changed the flight status to \033[0m", status_dic.get(status))


f = Flight("CA980")
f.flight_status
f.flight_status = 1
