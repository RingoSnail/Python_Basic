from multiprocessing import Process
import time
import random
import os


def task(name):
    print("%s is playing" % name)
    time.sleep(random.randrange(1, 10))
    print("%s play end" % name)


if __name__ == "__main__":
    p1 = Process(target=task, args=("1",))
    p2 = Process(target=task, args=("2",))
    p3 = Process(target=task, args=("3",))
    p4 = Process(target=task, args=("4",))

    p_l = [p1, p2, p3, p4]

    for p in p_l:
        p.start()
        p.join()
    # for p in p_l:
    #     p.join()  # 只有主进程会被阻塞，子进程之间并行

    print("主")
