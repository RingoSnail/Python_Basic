# 使用socketserver创建服务器程序时，如果使用fork或者线程服务器，
# 一个潜在的问题是，恶意的程序可能会发送大量的请求导致服务器崩溃，请写一个程序，避免此类问题
import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print("new connection:", self.client_address)
        while True:
            try:
                data = self.request.recv(1024)
                if not data:break
                print("client data:", data.decode())
                self.request.send(data.upper())
            except Exception as e:
                print(e)
                break


if __name__ == "__main__":
    sever = socketserver.ThreadingTCPServer(("127.0.0.1", 8080), Handler)
    sever.serve_forever()