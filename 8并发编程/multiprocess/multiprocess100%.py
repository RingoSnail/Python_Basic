from multiprocessing import Process


class Full(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        i = 2
        while True:
            pass


if __name__ == "__main__":
    f1 = Full("1")
    f2 = Full("2")
    f3 = Full("3")
    f4 = Full("4")
    f5 = Full("5")
    f6 = Full("6")
    f7 = Full("7")
    f8 = Full("8")

    f1.run()
    # f2.run()
    # f3.run()
    # f4.run()
    # f5.run()
    # f6.run()
    # f7.run()
    # f8.run()
