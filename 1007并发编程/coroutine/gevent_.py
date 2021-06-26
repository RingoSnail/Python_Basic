import gevent
from gevent import monkey;

monkey.patch_all()
import time


def eat(name):
    print("%s eat 1" % name)
    time.sleep(5)  # 模拟IO阻塞
    print("%s eat 2" % name)


def play(name):
    print("%s play 1" % name)
    time.sleep(3)
    print("%s play 2" % name)


g1 = gevent.spawn(eat, "egon")  # 协程对象
g2 = gevent.spawn(play, "alex")
gevent.joinall([g1, g2])

print("主")
