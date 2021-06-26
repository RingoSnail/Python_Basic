from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print("%s say hallo" % name)


if __name__ == "__main__":
    t = Thread(target=sayhi, args=("egon",))
    t.start()
    print("主")