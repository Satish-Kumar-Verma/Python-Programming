from abc import ABC, abstractmethod
import math


class Myclass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass


class Sub1(Myclass):
    def calculate(self, x):
        print(f"Square : {x * x}")


class Sub2(Myclass):
    def calculate(self, x):
        print(f"Square root : {math.sqrt(x)}")


class Sub3(Myclass):
    def calculate(self, x):
        print(f"Cube : {x ** 3}")


s1 = Sub1()
s1.calculate(2)

s2 = Sub2()
s2.calculate(9)

s3 = Sub3()
s3.calculate(4)
