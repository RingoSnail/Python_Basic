# 写一个程序，利用queue实现进程间通信
from multiprocessing import Process, Queue
import time, random, os


def consumer(q, name):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(random.randint(1, 3))
        print(f"{name},{res}")


def producer(q, name, food):
    for i in range(3):
        res = f"{food},{i}"
        q.put(res)
        print(f"{name}生产了{i}")


if __name__ == '__main__':
    q = Queue()
    # 生产者们:即厨师们
    p1 = Process(target=producer, args=(q, 'egon', '包子'))

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q, 'alex'))

    # 开始
    p1.start()
    c1.start()
    p1.join()
    q.put(None)
    print('主')
