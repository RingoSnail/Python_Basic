# Echo client program
import socket

HOST = "localhost"
PORT = 50007

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b'Hello, world')
#  b" "前缀表示：后面字符串是bytes 类型。用处：网络编程中，服务器和浏览器只认bytes 类型数据

data = client.recv(1024)

print("Received", data)