from socket import *
# import socket 与第一种引用相比需要socket.socket句点进行类的访问
import select

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 8093))
server.listen(5)
server.setblocking(False)  # 不被socket阻塞，只被select阻塞
print("starting...")

rlist = [server]
wlist = []
wdata = {}

while True:
    rl, wl, xl = select.select(rlist, wlist, [], 0.5)  # select将连接block，放入等待队列，超时时间0.5秒
    print(wl)
    for sock in rl:  # 轮询，同时处理多个连接
        if sock == server:
            conn, addr = sock.accept()
            rlist.append(conn)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                rlist.remove(sock)

    for sock in wl:
        sock.send(wdata[sock])
        wlist.remove(sock)
        wdata.pop(sock)
