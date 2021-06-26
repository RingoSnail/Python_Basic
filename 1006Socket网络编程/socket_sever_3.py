# Echo server program
import socket

HOST = ""
PORT = 50007

socket_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sever.bind((HOST, PORT))

socket_sever.listen(1)  # 允许一个连接排队

while True:  # 为每一个客户端循环生成对象
    conn, addr = socket_sever.accept()  # 为连接生成对象

    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            print("server recv:", conn.getpeername(), data.decode())
            if not data:break
            response = input(">>>").strip()  # 一来一往回复,其它情况会出bug
            conn.send(response.encode())
            # print("send to client", response)
