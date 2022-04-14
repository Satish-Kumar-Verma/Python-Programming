# Protected variables are available inside the class and its sub-classes


class A:
    def __init__(self, a):
        self._a = a

class B(A):
    def __init__(self, b):
        super().__init__(b)


b = B(34)
print(b._a)
