from threading import Thread, Semaphore
import threading
import time


def func():
    sm.acquire()
    print('%s get sm' % threading.current_thread().getName())
    time.sleep(5)
    sm.release()


if __name__ == "__main__":
    sm = Semaphore(5)  # 每次可以同时5个线程抢到锁
    for i in range(23):
        t = Thread(target=func)
        t.start()
