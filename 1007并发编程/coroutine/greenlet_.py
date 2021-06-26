from greenlet import greenlet


def eat(name):
    print("%s eat 1" % name)
    g2.switch("alex")  # 切换到g2，且传入alex
    print("%s eat 2" % name)
    g2.switch()


def play(name):
    print("%s play 1" % name)
    g1.switch()
    print("%s play 2" % name)


g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch("egon")  # 启动，且传入egon
