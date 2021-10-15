# Echo client program
import socket

HOST = "localhost"
PORT = 50007

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input(">>>").strip()
    if len(msg) == 0:continue
    if msg == "q": break
    client.sendall(msg.encode())  # 发

    data = client.recv(1024)      # 收，阻塞状态，收发只能交替进行，多开一个现程分开运行即可

    print("client recv", data.decode())