from threading import Thread


class MyThread(Thread):
    def __init__(self, str_):
        self.str = str_
        super().__init__()

    def display(self, x, y):
        print(self.str)
        print(f'Arguments are {x} and {y}.')


obj = MyThread("This is  the string!")
t1 = Thread(target=obj.display, args=(10, 20,))
t1.start()
