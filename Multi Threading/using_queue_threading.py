from threading import Thread
from time import sleep
from queue import Queue


class Producer:
    def __init__(self):
        self.item_queue = Queue()

    def produce(self):
        for i in range(1, 11):
            print(f"Producing the item : {i}")
            self.item_queue.put(i)
            sleep(0.4)


class Consumer:
    def __init__(self, producer_obj):
        self.producer_obj = producer_obj

    def consume(self):
        for i in range(1, 11):
            print(f'Receiving the item : {self.producer_obj.item_queue.get(i)}')


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
