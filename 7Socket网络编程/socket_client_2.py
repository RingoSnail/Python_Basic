# Echo client program
import socket

HOST = "localhost"
PORT = 50007

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input(">>>").strip()  # 循环发送
    if len(msg) == 0:continue

    client.sendall(msg.encode())  # bytes类型

    data = client.recv(1024)

    print("Received", data.decode())