# Echo server program
import socket

HOST = ""
PORT = 50007

socket_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sever.bind((HOST, PORT))

socket_sever.listen(1)  # 允许一个连接排队
conn, addr = socket_sever.accept()  # 为连接生成对象

with conn:
    print("Connected by", addr)
    while True:
        data = conn.recv(1024)
        if not data:break
        conn.sendall(data)  # 再发回去
