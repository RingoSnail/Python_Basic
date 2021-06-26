import random
import time
from multiprocessing import Process, JoinableQueue


def consumer(q, name):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[43m%s 吃 %s\033[0m' % (name, res))
        q.task_done()


def producer(q, name, food):
    for i in range(3):
        time.sleep(random.randint(1, 3))
        res = "%s%s" % (food, i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' % (name, res))
    q.join()


if __name__ == "__main__":
    q = JoinableQueue()

    p1 = Process(target=producer, args=(q, "egon1", "包子"))
    p2 = Process(target=producer, args=(q, 'egon2', '骨头'))
    p3 = Process(target=producer, args=(q, 'egon3', '泔水'))

    c1 = Process(target=consumer, args=(q, 'alex1'))
    c2 = Process(target=consumer, args=(q, 'alex2'))
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    p3.join()

    print("主")
