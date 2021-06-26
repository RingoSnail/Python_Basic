from threading import Thread
import time


def foo():
    print(123)
    time.sleep(5)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    t1.daemon = True  # 守护线程随时可能因主线程及其他线程结束而被回收
    t1.start()
    t2.start()
    print("main-------")  # 主线程会等着其他非守护线程结束才结束，再回收守护线程
