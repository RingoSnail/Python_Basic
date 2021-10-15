# # 顺序执行
# import time
#
#
# def f1():
#     res = 1
#     for i in range(100000000):
#         res += i
#
#
# def f2():
#     res = 1
#     for i in range(100000000):
#         res *= i
#
#
# start = time.time()
# f1()
# f2()
# stop = time.time()
# print('run time is %s' % (stop - start))  # 10.985628366470337
# 切换
from greenlet import greenlet
import time


def f1():
    res = 1
    for i in range(100000000):
        res += i
        g2.switch()


def f2():
    res = 1
    for i in range(100000000):
        res *= i
        g1.switch()


start = time.time()
g1 = greenlet(f1)
g2 = greenlet(f2)
g1.switch()
stop = time.time()
print('run time is %s' % (stop - start))  # 52.763017892837524
# 单纯的切换（在没有io的情况下或者没有重复开辟内存空间的操作），反而会降低程序的执行速度
