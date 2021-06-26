from multiprocessing import Process, Lock
import time, json
# 再看下json


def serach(name):
    dic = json.load(open("C:/Users/Ringo/PycharmProjects/Python_Basic/1007并发编程/multiprocess/db"))
    time.sleep(1)
    print("\033[43m%s 查到剩余票数%s\033[0m" % (name, dic["count"]))


def get(name):
    dic = json.load(open("C:/Users/Ringo/PycharmProjects/Python_Basic/1007并发编程/multiprocess/db"))
    time.sleep(1)
    if dic["count"] > 0:
        dic["count"] -= 1
        time.sleep(1)
        json.dump(dic, open("C:/Users/Ringo/PycharmProjects/Python_Basic/1007并发编程/multiprocess/db", "w"))
        print("\033[46m%s 购票成功\033[0m" % name)


def task(name, lock):
    serach(name)
    with lock:
        get(name)  # 购票变成了串行


if __name__ == "__main__":
    lock = Lock()
    for i in range(10):  # 模拟并发10个客户端抢票
        name = "<路人%s>" % i
        p = Process(target=task, args=(name,lock))
        p.start()

        # p.join() 不要用jion()，因为会使整个线程阻塞，而查票是不需要阻塞的
