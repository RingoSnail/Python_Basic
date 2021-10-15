from threading import Thread, Lock
import time

mutexA = Lock()
mutexB = Lock()


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' % self.name)

        mutexB.acquire()
        print('\033[41m%s 拿到B锁\033[0m' % self.name)
        mutexB.release()  # 全部取到才能释放

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[41m%s 拿到B锁\033[0m' % self.name)

        time.sleep(2)  # 等两秒再取A，此时Thread-2已取到A，但B已被Thread-1取到，Thread-2无法执行下去释放A
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' % self.name)
        mutexA.release()

        mutexB.release()  # B也无法被释放


if __name__ == "__main__":
    for i in range(10):
        t = MyThread()
        t.start()
