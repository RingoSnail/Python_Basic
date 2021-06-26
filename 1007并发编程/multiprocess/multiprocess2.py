import time
import random
from multiprocessing import Process


class Play(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s playing' % self.name)
        a = random.randrange(1, 10)
        print(a)
        time.sleep(a)
        print(time.localtime())
        print('%s play end' % self.name)


if __name__ == '__main__':
    # 实例化得到四个对象
    p1 = Play('Egon')
    p2 = Play('Alex')
    p3 = Play('Ringo')
    p4 = Play('Yuan')
    # 调用对象下的方法，开启四个进程
    p1.start()  # start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主')
