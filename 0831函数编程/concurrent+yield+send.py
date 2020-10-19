import time  # 通过yield, 我们可以实现单核下并发做多件事的效果。


def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield  # yield可以接收到外部send传过来的数据并赋值给baozi
        print("包子[%s]来了,被[%s]吃了!" % (baozi, name))


c = consumer('A')
c2 = consumer('B')
c.__next__()  # 执行一下next可以使上面的函数走到yield那句。 这样后面的send语法才能生效
c2.__next__()
print("----老子开始准备做包子啦!----")
for i in range(10):
    time.sleep(1)
    print("做了2个包子!")
    c.send(i)  # send的作用=next, 同时还把数据传给了上面函数里的yield
    c2.send(i)
