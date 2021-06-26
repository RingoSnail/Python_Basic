def start(ip_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ip_port)
    client.send(f"{currentThread().getName()} hello".encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))


if __name__ == '__main__':
    import socket
    from threading import Thread, currentThread

    ip_port = ('127.0.0.1', 8082)
    for i in range(20):
        t = Thread(target=start, args=(ip_port,))
        t.start()
