from threading import Thread
import threading
from multiprocessing import Process
import os
import time


def work():
    time.sleep(3)
    print("子线程", threading.current_thread().getName())


if __name__ == "__main__":
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    t1.join()  # 两个子线程之间并不阻塞，只对主线程阻塞
    t2.join()

    time.sleep(3)
    print(threading.current_thread().getName())  # 主线程
    print(threading.current_thread())
    print(threading.enumerate())
    print(threading.active_count())
    print("主线程")
