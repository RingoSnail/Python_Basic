# 开启新线程开销远远小于开启新进程

from multiprocessing import Process


def work():
    print('hallo')


if __name__ == '__main__':
    # 在主进程下开启子进程
    p = Process(target=work)
    p.start()
    print('主进程')
#
# from threading import Thread
#
#
# def work():
#     print('hallo')
#
#
# if __name__ == '__main__':
#     t = Thread(target=work)
#     t.start()
#     print('主线程')
