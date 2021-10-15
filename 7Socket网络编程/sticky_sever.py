import socket
import subprocess
ip_port = ('127.0.0.1', 8080)
tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)
while True:
    conn, addr = tcp_socket_server.accept()
    print('客户端', addr)
    while True:
        cmd = conn.recv(1024)
        if len(cmd) == 0: break
        print("recv cmd",cmd)
        subprocess
        # 模块允许我们启动一个新进程，并连接到它们的输入 / 输出 / 错误管道，从而获取返回值。
        res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stderr = res.stderr.read()
        stdout = res.stdout.read()
        print("res length",len(stdout))
        conn.send(stderr)
        conn.send(stdout)