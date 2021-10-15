from multiprocessing import Process
import time
import random


def task(name):
    print('%s is piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s is piao end' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('egon',), name="子进程1")
    p1.start()
    p1.join()
    p1.terminate()  # 关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
    print(p1.is_alive())  # 结果为True
    print('主')
    print(p1.is_alive())  # 结果为False
    print(p1.name, p1.pid)
