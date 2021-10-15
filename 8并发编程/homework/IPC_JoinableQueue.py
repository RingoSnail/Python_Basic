from multiprocessing import Process, JoinableQueue
import time, random, os


def producer(q, name):
    for i in range(3):
        res = f"{name},{i}"
        q.put(res)
        print(res)


def consumer(q, name):
    while True:
        res = q.get()
        print(f'{name} eating---', res)
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=(q, 'aa'))
    c1 = Process(target=consumer, args=(q, 'bb'))
    c1.daemon = True
    p1.start()
    c1.start()
    p1.join()
    print('主')
