from threading import Thread
from socket import *
import threading


def client(sever_ip, port):
    c = socket(AF_INET, SOCK_STREAM)
    c.connect((sever_ip, port))

    count = 0
    while True:
        c.send(("%s say hello %s" %(threading.current_thread().getName(), count)).encode("utf-8"))
        msg = c.recv(1024)
        print(msg.decode("utf-8"))  # 接收并打印
        count += 1


if __name__ == "__main__":
    for i in range(500):
        t = Thread(target=client, args=("127.0.0.1", 8080))
        t.start()
