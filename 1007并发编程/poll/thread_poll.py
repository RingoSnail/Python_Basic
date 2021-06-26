import os
import random
import time
from concurrent.futures import ThreadPoolExecutor


def task(n):
    print("%s is running" % os.getpid())
    time.sleep(random.randint(3, 5))
    return n**2


if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=3)  # 线程池内只能有三个线程
    futures = []
    for i in range(11):
        future = executor.submit(task, i)
        futures.append(future)
    executor.shutdown(True)
    print("+++>")
    for future in futures:
        print(future.result())
