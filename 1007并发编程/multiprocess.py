import time
import random
from multiprocessing import Process


def play(name):
    print("%s is playing" % name)
    a = random.randrange(1, 10)
    print(a)
    time.sleep(a)
    print(time.localtime())
    print("%s play end" % name)


if __name__ == '__main__':  # Process必须放在这个下
    p1 = Process(target=play, args=('Egon',))  # 必须加,号
    p2 = Process(target=play, args=('Alex',))
    p3 = Process(target=play, args=('Ringo',))
    p4 = Process(target=play, args=('Yuan',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print("主")
