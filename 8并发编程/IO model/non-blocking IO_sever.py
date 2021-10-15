from socket import *
server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1',8099))
server.listen(5)
server.setblocking(False)  # 设置socket为非阻塞
rlist=[]  # readlist
wlist=[]  # writelist
while True:
    try:
        conn, addr = server.accept()
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:
        del_rlist=[]
        for sock in rlist:
            try:
                data=sock.recv(1024)
                if not data:
                    del_rlist.append(sock)
                wlist.append((sock,data.upper()))
            except BlockingIOError:
                continue
            except Exception:
                sock.close()
                del_rlist.append(sock)
        del_wlist=[]
        for item in wlist:
            try:
                sock = item[0]
                data = item[1]
                sock.send(data)
                del_wlist.append(item)
            except BlockingIOError:
                pass
        for item in del_wlist:
            wlist.remove(item)
        for sock in del_rlist:
            rlist.remove(sock)
server.close()