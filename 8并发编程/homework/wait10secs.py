# 写一个程序，包含十个线程，子线程必须等待主线程sleep 10秒钟之后才执行，并打印当前时间
from threading import Thread, Event, currentThread
import time, datetime


def task():
    print(f"{currentThread().getName()}等待")
    event.wait()
    print(f"{currentThread().getName()}, {datetime.datetime.now()} is running")


if __name__ == "__main__":
    event = Event()
    for i in range(10):
        t = Thread(target=task)
        t.start()
    time.sleep(10)
    event.set()  # 状态值设为True，阻塞的线程进入激活状态
