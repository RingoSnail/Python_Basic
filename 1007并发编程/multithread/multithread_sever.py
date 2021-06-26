from socket import *
from threading import Thread


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def servers(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        print(conn, addr)
        t = Thread(target=communicate, args=(conn,))
        t.start()
    server.close()


if __name__ == "__main__":
    servers("127.0.0.1", 8081)
