import random
import time
from multiprocessing import Process, Queue


def consumer(q, name):
    while True:
        res = q.get()
        if res is None:break
        time.sleep(random.randint(1, 3))
        print('\033[43m%s 吃 %s\033[0m' % (name, res))


def producer(q, name, food):
    for i in range(1, 4):
        time.sleep(random.randint(1, 3))
        res = "%s%s" % (food, i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' % (name, res))


if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q, "egon", "包子"))

    c1 = Process(target=consumer, args=(q, "alex"))

    p1.start()
    c1.start()

    p1.join()
    q.put(None)  # 结束信号

    print("主")
