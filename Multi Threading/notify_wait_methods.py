from threading import Thread, Condition
from time import sleep


class Producer:
    def __init__(self):
        self.lst = []
        self.condition_var = Condition()

    def produce(self):
        self.condition_var.acquire()

        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print(f"{i} items produced...")

        self.condition_var.notify()
        self.condition_var.release()
        print("All Items produced!")


class Consumer:
    def __init__(self, producer):
        self.producer = producer

    def consume(self):
        self.producer.condition_var.acquire()

        self.producer.condition_var.wait(timeout=0)

        print(self.producer.lst)
        self.producer.condition_var.release()


p = Producer()
c = Consumer(p)

thread_1 = Thread(target=p.produce)
thread_2 = Thread(target=c.consume)

thread_1.start()
thread_2.start()
