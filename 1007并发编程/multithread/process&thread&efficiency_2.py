from multiprocessing import Process
from threading import Thread
import threading
import os, time


def work():  # I/O密集型任务
    time.sleep(2)
    print('===>')


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 本机为16核
    start = time.time()
    for i in range(400):
        p = Process(target=work)  # 大部分时间耗费在创建进程上
        # p = Thread(target=work)  # 效率高
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print('run time is %s' % (stop - start))
