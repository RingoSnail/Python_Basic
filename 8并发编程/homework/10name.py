# 请写一个包含10个线程的程序，并给每一个子线程都创建名为"name"的线程私有变量，变量值为“Alex”
from threading import Thread


def task(name):
    print(name, "is running")


if __name__ == '__main__':
    for i in range(10):
        name = f"alex{i}"
        t = Thread(target=task, args=(name, ))
        t.start()
    print("主end")