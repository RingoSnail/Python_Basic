from threading import Thread, RLock
import time

mutexA = mutexB = RLock()
# 一个线程拿到锁，counter加1,该线程内又获得其他锁，则counter继续加1，
# 等待该线程释放所有锁，即counter递减到0之前，所有其他线程都只能等待。


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' % self.name)
        mutexB.acquire()
        print('\033[41m%s 拿到B锁\033[0m' % self.name)
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[42m%s 拿到B锁\033[0m' % self.name)
        time.sleep(2)
        mutexA.acquire()
        print('\033[42m%s 拿到A锁\033[0m' % self.name)
        mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
