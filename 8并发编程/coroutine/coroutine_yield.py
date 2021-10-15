# 串行执行
# import time
#
#
# def consumer(res):
#     pass
#
#
# def producer():
#     res = []
#     for i in range(10000000):
#         res.append(i)
#     return res
#
#
# start = time.time()
# res = producer()
# consumer(res)
# stop = time.time()
# print(stop-start)


# 基于yield并发执行
import time


def consumer():
    while True:
        x = yield


def producer():
    g = consumer()  # 反复切换 模拟并发，实际降低了效率
    next(g)
    for i in range(10000000):
        g.send(i)
        time.sleep(2)


start = time.time()
producer()
stop = time.time()
print(stop-start)
