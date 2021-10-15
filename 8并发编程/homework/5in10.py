# 写一个程序，包含十个线程，同时只能有五个子线程并行执行
from threading import Thread, Semaphore, currentThread
import time


def task():
    sm.acquire()
    print(currentThread().getName())
    time.sleep(2)
    sm.release()


if __name__ == "__main__":
    sm = Semaphore(5)
    start = time.time()
    for i in range(10):
        t = Thread(target=task)
        t.start()
    t.join()
    stop = time.time()
    print(stop - start)