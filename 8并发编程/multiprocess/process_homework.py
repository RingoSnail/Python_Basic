from multiprocessing import Process
import time
import random


def task(n):
    time.sleep(random.randint(1, 5))
    print('-------->%s' % n)


if __name__ == '__main__':
    p1 = Process(target=task, args=(1,))
    p2 = Process(target=task, args=(2,))
    p3 = Process(target=task, args=(3,))

    p1.start()
    p1.join()  # 串行

    p2.start()
    p2.join()

    p3.start()
    p3.join()


    print('-------->4')
