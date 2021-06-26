from multiprocessing import Process
import time
import random
import os


def task():
    print("%s is playing" % os.getpid())
    time.sleep(random.randrange(1, 3))
    print("%s play end" % os.getpid())


if __name__ == "__main__":
    p = Process(target=task)
    p.start()
    p.join()  # 主线程会阻塞，等到此子线程结束才继续执行，而其他子进程不阻塞
    print("主")
