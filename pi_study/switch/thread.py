from threading import Thread
from time import sleep


def fx1():
    while True:
        print(f"fx1")
        sleep(1)


def fx2():
    while True:
        print(f"fx2")
        sleep(1)


def fx3():
    for i in range(10):
        print(f"fx3 - {i}")
        sleep(1)


def fx4():
    for i in range(10):
        print(f"fx4 - {i}")
        sleep(1)


if __name__ == "__main__":
    thread1 = Thread(target=fx3, daemon=True)
    thread2 = Thread(target=fx4, daemon=True)
    thread1.start()
    thread2.start()
    print("메인 종료")








