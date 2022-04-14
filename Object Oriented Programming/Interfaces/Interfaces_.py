from abc import ABC, abstractmethod


class MyClass(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class Oracle(MyClass):
    def connect(self):
        print("Connected to the oracle database...")

    def disconnect(self):
        print("Disconnected from the oracle database.")


class MySQL(MyClass):
    def connect(self):
        print("Connected to the MySQL database...")

    def disconnect(self):
        print("Disconnected from the MySQL database.")


class Database:
    str = input("Enter the database name : ")
    class_name = globals()[str]

    x = class_name()
    x.connect()
    x.disconnect()


# o = Oracle()
# o.connect()
# o.disconnect()
#
# m = MySQL()
# m.connect()
# m.disconnect()


#  Note : we cannot create objects of abstract classes / Interfaces

# camelCase
#