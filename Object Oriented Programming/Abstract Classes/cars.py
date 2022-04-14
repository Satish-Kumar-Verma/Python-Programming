from abc import ABC, abstractmethod


class Car(ABC):  # classes which have abstract methods and concrete methods are abstract classes
    def __init__(self, reg_no):
        self.reg_no = reg_no

    def openTank(self):  # concrete method
        print("Adding fuel to the tank!")
        print("Done!")

    @abstractmethod
    def steering(self):  # abstract method
        pass

    @abstractmethod
    def braking(self):  # abstract method
        pass


class Maruti(Car): # is - a relationship
    def steering(self):
        print("Maruti has manual steering!")

    def braking(self):
        print("Maruti has hydraulic brake!")


class Santro(Car):
    def steering(self):
        print("Santro has power steering!")

    def braking(self):
        print("Santro has gas brake!")


m = Maruti(123)
m.openTank()
m.steering()
m.braking()

s = Santro(124)
s.openTank()
s.steering()
s.braking()

c = Car(1222)
c.openTank()
