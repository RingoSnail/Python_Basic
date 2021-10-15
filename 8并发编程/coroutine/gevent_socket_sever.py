from gevent import monkey;monkey.patch_all()
from socket import *
import gevent


def sever(sever_ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((sever_ip, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        gevent.spawn(talk, conn, addr)  # 开启协程


def talk(conn, addr):
    try:
        while True:
            res = conn.recv(1024)
            print("client %s: %s msg: %s" % (addr[0], addr[1], res))  # 接收并打印地址、端口、内容
            conn.send(res.upper())  # 发回大写版
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == "__main__":
    sever("127.0.0.1", 8080)
