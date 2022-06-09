from threading import *
from time import sleep


class Theatre:
    def __init__(self, str):
        self.str = str

    def movie_show(self):
        for i in range(1, 6):
            print(f"{self.str} : loop no.{i} of {current_thread().name}")
            sleep(0.1)


obj1 = Theatre("Cut Ticket")
obj2 = Theatre("Show Chair")

t1 = Thread(target=obj1.movie_show)
t2 = Thread(target=obj2.movie_show)

t1.__setattr__("name", "Thread-1")
t2.__setattr__("name", "Thread-2")

t1.start()
t2.start()
