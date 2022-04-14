class A:
    def __init__(self, value, value2):
        self.value = value
        self.another_value = value2

    def __add__(self, other):
        return self.another_value + other.value


a = A(3, 4)
b = A(6, 12)
print(a + b)
