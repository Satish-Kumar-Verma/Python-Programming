from threading import Thread, current_thread, Lock
# from threading import Semaphore
from time import sleep


class Train:
    def __init__(self, available):
        self.available_berth = available
        self.lock = Lock()
        # self.lock = Semaphore() // Lock() and Semaphore() are use for synchronization the threads

    def reserve(self, wanted):
        self.lock.acquire()
        print(f"No. of available berth : {self.available_berth}")
        if self.available_berth >= wanted:
            sleep(2)
            self.available_berth -= wanted
            print(f"{current_thread().name} allotted the berth!")
        else:
            print("Berth is not available!")

        self.lock.release()


train = Train(2)

akm = Thread(target=train.reserve, args=(2,))
khant = Thread(target=train.reserve, args=(1,))

akm.__setattr__("name", "Ar Kar Min")
khant.__setattr__("name", "Khant Pyae Phyo")

akm.start()
khant.start()
