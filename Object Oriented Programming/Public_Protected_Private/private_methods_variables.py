# Private variables/methods are only accessible inside the class

class Testing:
    __var = 10
    def __init__(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def getName(self):
        # return self.__get_name()
        return self.__name

    @classmethod
    def get_var(cls):
        return cls.__var

    @staticmethod
    def get_v():
        return Testing.__var

    @classmethod
    def set_var(cls, val):
        cls.__var = val

    @staticmethod
    def set_v(val):
        Testing.__var = val


t = Testing("Hello")

# print(t.getName())

# print(Testing.__var)
# t.set_var(12)
# Testing.set_var(14)
# t.set_v(23)
# Testing.set_v(25)
# print(t.get_v())
# print(t.get_var())
# print(Testing.get_v())
# print(Testing.get_var())

























# print(t.__name)
# print(t.__get_name())
print(t.getName())
# print(Testing.__var)
print(Testing.get_var())
# print(t._Testing__get_name())  # obj._class__get_name()

# print(t._Testing__name)