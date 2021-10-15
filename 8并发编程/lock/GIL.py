import time
from threading import Thread, Lock


def work():
    global n
    lock.acquire()  # 加锁保证数据被每个线程逐个修改
    time.sleep(0.1)
    n -= 1
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    n = 100
    l = []
    for i in range(50):  # 创建100个线程
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()  # 阻塞，等待所有线程执行完再执行下一步主线程
    print(n)  # 结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全，不加锁则不知道数据会被线程按哪种顺序修改
