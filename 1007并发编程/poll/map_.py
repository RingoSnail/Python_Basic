import os
import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def task(n):
    print("%s is running" % os.getpid())
    time.sleep(random.randint(1, 3))
    return n**2


if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=3)
    executor.map(task, range(0, 11))

    # map方法取代如下代码
    # for i in range(11):
    #     future = executor.submit(task, i)
