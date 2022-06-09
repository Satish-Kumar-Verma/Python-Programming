from time import sleep
from threading import Thread


class MyThread:
    def __init__(self):
        pass

    def prepare_tea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Boil milk and tea powder for 5 minutes...", end="")
        sleep(5)
        print("Done!")

    def task2(self):
        print("Add suger and boil for 3 minutes...", end="")
        sleep(3)
        print("Done!")

    def task3(self):
        print("Filtering...", end="")
        sleep(1)
        print("Served!")


obj = MyThread()

t = Thread(target=obj.prepare_tea)
t.start()
t.join()
