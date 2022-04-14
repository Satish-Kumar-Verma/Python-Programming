
class Person:
    testing = 4

    def __init__(self, name):
        self.name = name
        self.age = "21"

    def __str__(self):
        return f"I am {self.name} and I am {self.age} years old!"

    class DOB:
        def __init__(self):
            self.day = 2
            self.month = 2
            self.year = 2020


p1 = Person("AKM")
p2 = Person("KPP")
dob = p1.DOB()
print(dob.year)
print(p1)
print(p2)
Person.testing = 5
p1.age = 23
print(p1.age)
print(p2.age)
print(p1.testing)
print(p2.testing)
