import sys
from threading import *
import threading
import time
import sys


def display(str_):
    print(str_)
    print(threading.current_thread().__getattribute__('name'))


def animate():
    i = 0
    while i < 10:
        counter = 1
        sys.stdout.write('\r.' * counter)
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('.' * counter)
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('.' * counter)
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('.' * counter)
        sys.stdout.flush()
        time.sleep(1)


print(threading.current_thread().__getattribute__('name'))
for i in range(5):
    t = Thread(target=display, args=("Hi",))
    t.start()

    if i == 2:
        t2 = Thread(target=animate)
        t2.start()
