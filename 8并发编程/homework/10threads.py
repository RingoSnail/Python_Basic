# 请写一个包含10个线程的程序，主线程必须等待每一个子线程执行完成之后才结束执行，每一个子线程执行的时候都需要打印当前线程名、当前活跃线程数量
from threading import Thread, currentThread, activeCount
import time


def task(n):
    print("线程名：%s----%s" % (currentThread().name, n))
    time.sleep(3)
    print("数量：%s" % activeCount())


if __name__ == "__main__":
    t_li = []
    for i in range(10):
        t = Thread(target=task, args=(i, ))
        t.start()
        t_li.append(t)
    for t in t_li:
        t.join()

    print("主, end----")
