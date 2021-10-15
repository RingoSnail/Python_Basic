# 写一个程序，使用socketserver模块，实现一个支持同时处理多个客户端请求的服务器，要求每次启动一个新线程处理客户端请求
import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print("new connection:", self.client_address)
        with True:
            try:
                data = self.request.recv(1024)
                if not data: return
                print("client data:", data.decode())
                self.request.send(data.upper())
            except Exception as e:
                print(e)
                return


if __name__ == "__main__":
    sever = socketserver.ThreadingTCPServer(("127.0.0.1", 8080), Handler)
    sever.serve_forever()
