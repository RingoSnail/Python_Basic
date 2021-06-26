import random
import threading
import time
from threading import Thread, Event


def conn_mysql():
    count = 1
    while not event.is_set():  # 检查Event状态值
        if count > 3:
            raise TimeoutError('链接超时')
        print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
        event.wait(0.5)
        count += 1
    print('<%s>链接成功' % threading.current_thread().getName())


def check_mysql():
    print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
    time.sleep(random.randint(2, 4))
    event.set()  # 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态，等待操作系统调度


if __name__ == '__main__':
    event = Event()
    conn1 = Thread(target=conn_mysql)
    conn2 = Thread(target=conn_mysql)
    check = Thread(target=check_mysql)
    conn1.start()
    conn2.start()
    check.start()
