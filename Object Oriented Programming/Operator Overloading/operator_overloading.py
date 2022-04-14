# a = 3
# b = 5
# print(a + b)
# print(type(a))
# print(type(b))

class A(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return self.value * other.value

    def __lt__(self, other):
        return self.value < other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __iadd__(self, other):
        self.value += other.value
        # self.value = self.value + other.value
        return self.value


class B:
    def __init__(self, value):
        self.value = value


a = A(10)
b = B(11)
print(a + b)
print(a * b)
print(a < b)
print(a / b)
a += b
print(a)
