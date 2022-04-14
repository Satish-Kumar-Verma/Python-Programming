from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_it(self, text):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class IBM(Printer):
    def print_it(self, text):
        print(text)

    def disconnect(self):
        print('Printing complete on IBM printer!')


class Epson(Printer):
    def print_it(self, text):
        print(text)

    def disconnect(self):
        print("Printing complete on Epson printer!")


class UsePrinter:
    with open("config.txt", "r") as f:
        # f.seek(5)
        data = f.readline().strip('\n')
    # data = input("Printer name : ")

    class_name = globals()[data]

    obj = class_name()
    obj.print_it("Printing!")
    obj.disconnect()
