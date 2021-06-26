import socket

ip_port = ("127.0.0.1", 9000)
BUFSIZE = 1024
udp_sever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp类型

udp_sever.bind(ip_port)

while True:  # UDP不用listen，直接收发
    msg, addr = udp_sever.recvfrom(BUFSIZE)
    print("recv", msg, addr)
    if not msg:break

    udp_sever.sendto(msg.upper(), addr)