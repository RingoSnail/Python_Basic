from multiprocessing import Process, Lock
import os, time


def work(lock):
    lock.acquire()  # 加锁
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())
    lock.release()  # 释放锁


if __name__ == '__main__':
    lock = Lock()  # 变为串行
    for i in range(3):
        p = Process(target=work, args=(lock,))
        p.start()
