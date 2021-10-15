# Echo server program
import socket

HOST = ""
PORT = 50007

socket_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sever.bind((HOST, PORT))

socket_sever.listen(2)  # 允许两个连接等待排队

count = 0  # 记录是第几次连接
while True:  # 为每一个客户端循环生成对象
    conn, addr = socket_sever.accept()  # 为连接生成对象
    count += 1
    print(f"[{count}] - got a new connection: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            print("server recv:", conn.getpeername(), data.decode())
            if not data:break
            conn.send(data.upper())

socket_sever.close()
