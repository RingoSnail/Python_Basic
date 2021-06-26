from multiprocessing import Process, Queue
import time, random, os


# 多个生产者参与者
def consumer(q, name):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(random.randint(1, 3))
        print('\033[43m%s 吃 %s\033[0m' % (name, res))


def producer(q, name, food):
    for i in range(1, 4):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (food, i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' % (name, res))


if __name__ == '__main__':
    q = Queue()
    # 生产者们:即厨师们
    p1 = Process(target=producer, args=(q, 'egon1', '包子'))
    p2 = Process(target=producer, args=(q, 'egon2', '骨头'))
    p3 = Process(target=producer, args=(q, 'egon3', '泔水'))
    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q, 'alex1'))
    c2 = Process(target=consumer, args=(q, 'alex2'))
    # 开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    q.put(None)
    print('主')
