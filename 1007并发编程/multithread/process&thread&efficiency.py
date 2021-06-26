from multiprocessing import Process
from threading import Thread
import os, time


def work():  # 计算密集型任务
    res = 0
    for i in range(100000000):
        res *= i


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 本机为16核
    start = time.time()
    for i in range(4):
        # p = Process(target=work)  # 多进程效率高
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print('run time is %s' % (stop - start))
