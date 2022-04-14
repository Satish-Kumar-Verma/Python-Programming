

class A:
    def __init__(self):
        self.a = "a"
        print(self.a)
        super().__init__()


class B:
    def __init__(self):
        self.b = "b"
        print(self.b)
        super().__init__()


class C(A, B):
    def __init__(self):
        self.c = "c"
        print(self.c)
        super().__init__()


c = C()
