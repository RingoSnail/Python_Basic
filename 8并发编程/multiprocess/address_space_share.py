# from multiprocessing import Process
# import os
#
#
# def work():
#     global n
#     n = 0
#
#
# if __name__ == '__main__':
#     n = 100
#     p = Process(target=work)
#     p.start()
#     p.join()
#     print('主', n)


from threading import Thread
import os


def work():
    global n
    n = 0


if __name__ == '__main__':
    n = 100
    t = Thread(target=work)
    t.start()
    t.join()
    print('主', n)
