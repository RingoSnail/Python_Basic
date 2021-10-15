# 使用selectors模块创建一个处理客户端消息的服务器程序
import socket
import selectors

# IO多路复用 selectors 会根据操作系统选择select poll epoll
sel = selectors.DefaultSelector()


def accept(sever_fileobj, mask):
    conn, addr = sever_fileobj.accept()
    print(addr)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    try:
        data = conn.recv(1024)
        if not data:
            print("closing...", conn)
            sel.unregister(conn)
            conn.close()
            return
        conn.send(data.upper())
    except Exception:
        print("closing...", conn)
        sel.unregister(conn)
        conn.close()


sever_fileobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_fileobj.bind(("127.0.0.1", 8080))
sever_fileobj.listen(5)
sever_fileobj.setblocking(False)
sel.register(sever_fileobj, selectors.EVENT_READ, accept)
while True:
    events = sel.select()
    for sel_obj, mask in events:
        callback = sel_obj.data
        callback(sel_obj.fileobj, mask)
