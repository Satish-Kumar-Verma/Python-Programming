from threading import Thread
from time import sleep


class Producer:
    def __init__(self):
        self.lst = []
        self.dataprodover = False

    def produce(self):
        for i in range(1, 11):
            self.lst.append(i)
            sleep(1)
            print(f"{i} items produced..")

        self.dataprodover = True


class Consumer:
    def __init__(self, producer):
        self.producer = producer

    def consume(self):
        while self.producer.dataprodover == False:
            sleep(0.1)

        print(self.producer.lst)


p = Producer()
c = Consumer(p)

thread_1 = Thread(target=p.produce)
thread_2 = Thread(target=c.consume)

thread_1.start()
thread_2.start()
