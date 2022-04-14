import math


class Square:
    def __init__(self):
        self.temp = 2

    def set_temp(self, val):
        self.temp = val

    def area(self, x):
        print(x * x)


class Circle(Square):
    # def area(self, x):
    #     print(math.pi * x * x)
    def __init__(self):
        super().__init__()
        self.testing = None

    def testing_(self):
        self.testing = self.temp


c = Circle()
# c.area(2)
print(c.temp)

c.testing_()
print(c.testing)
c.set_temp(6)
print(c.temp)

# s = Square()
# s.area(4)
