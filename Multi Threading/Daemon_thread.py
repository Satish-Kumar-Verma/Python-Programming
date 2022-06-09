from threading import Thread
from time import ctime, sleep


def display():
    for i in range(1, 6):
        print(i)
        sleep(1)


def display_time():
    while True:
        print(ctime())
        sleep(2)


thread_1 = Thread(target=display)
thread_1.start()

thread_2 = Thread(target=display_time)
thread_2.daemon = True

thread_2.start()
thread_2.join()
