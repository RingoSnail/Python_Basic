from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    t.setDaemon(True)  # 必须在t.start()之前设置
    t.start()
    # print(t.is_alive())
    print('主线程')
    print(t.is_alive())
    # 主进程结束，线程被回收
