# 请使用协程写一个消费者生产者模型
# import gevent
# from gevent import monkey;monkey.patch_all()
#
#
# def consumer(i):
#     print("消费", i)
#
#
# def producer(i):
#     print("生产", i)
#
#
# if __name__ == "__main__":
#     for i in range(10):
#         g1 = gevent.spawn(producer, i)
#         g2 = gevent.spawn(consumer, i)
#         g1.join()
#         g2.join()


def consumer():
    while True:
        x = yield
        print("消费", x)


def producer():
    c = consumer()
    next(c)
    for i in range(10):
        print("生产", i)
        c.send(i)


producer()