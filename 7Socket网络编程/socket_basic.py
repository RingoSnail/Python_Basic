import socket

# socket实例
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)

socket.AF_UNIX  # 进程间通信
socket.AF_INET  # 网络通信
socket.SOCK_STREAM  # for tcp
socket.SOCK_DGRAM  # for udp
socket.SOCK_RAW  # 原始套接字 可以处理ICMP IGMP IPV4
socket.SOCK_RDM  # 一种可靠的UDP形式

# socket函数
# 服务端
s.bind()  # 绑定
s.listen()  # 监听
s.accept()  # 阻塞式接受

# 客户端
s.connect()  # 建立链接
s.connect_ex()  # 扩展，出错时抛出错码

# 公共用途的套接字函数
s.recv()  # 接收数据
s.send()  # 发送数据，待发送数据量大于己端缓存区剩余空间时，数据丢失，不会发完
s.sendall()  # 循环发送，不丢失
s.recvfrom()
s.getpeername()  # 获得远端的地址
s.close()
socket.setblocking(flag)  # 设置IO阻塞模式，TRUE OR FALSE
socket.getaddrinfo(host=1008, port=8001, family=0, proto=0, flags=0)  # 返回远程主机的地址信息
socket.getfqdn()  # 拿到本机的主机名
socket.gethostbyname()  # 通过域名解析地址
