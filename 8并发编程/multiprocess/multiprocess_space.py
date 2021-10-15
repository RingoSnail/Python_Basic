from multiprocessing import Process

# 各进程空间彼此隔离
n = 100


def work():
    global n
    n = 0
    print("子进程内：", n)


if __name__ == "__main__":

    p = Process(target=work)  # work不能加（）
    p.start()
    print("主进程内", n)

