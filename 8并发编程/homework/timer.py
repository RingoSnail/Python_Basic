# 写一个程序 ，包含一个名为hello的函数，函数的功能是打印字符串“Hello, World!”，该函数必须在程序执行30秒之后才开始执行(不能使用time.sleep())
# from threading import Timer
#
#
# def hello(name):
#     print("%s say " % name, "Hello World!")
#
#
# if __name__ == "__main__":
#     t = Timer(5, hello, args=("alice", ))
#     t.start()


from threading import Thread, Timer, currentThread, Event


def task():
    event.wait()
    print("Hello World!")


if __name__ == "__main__":
    event = Event()
    t = Thread(target=task)
    t.start()
    event.wait(5)
    event.set()
