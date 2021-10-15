# 写一个程序，利用pipe实现进程间通信
from multiprocessing import Process, Pipe


def task(conn):
    conn.send("Hello World!")
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=task, args=(child_conn, ))
    p.start()
    p.join()
    print(parent_conn.recv())
