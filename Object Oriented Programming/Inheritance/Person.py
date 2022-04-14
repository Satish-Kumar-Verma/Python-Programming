# "is a" relationship | can be inherited


class Person:  # Person is a super class / base class
    def __init__(self):
        self.name = None
        self.age = None
        self.height = None

    def speak(self):
        print("I can speak!")

    def eat(self):
        print("I can eat!")


class Student(Person):  # student is a sub class

    def skip_school(self):
        print("I can skip school!")

    def __str__(self):
        return f"{self.name}, {self.age}"


s = Student()
s.name = "Hla"
s.age = 22
s.speak()
s.skip_school()
print(s)


p = Person()
p.name = "H"
# p.skip_school()  Not accessible
