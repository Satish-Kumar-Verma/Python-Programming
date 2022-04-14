import pickle  # Serialization


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name}. And I am {self.age} years old!"


p = Person("AKM", 21)
with open("person_info.dat", "wb") as f:
    pickle.dump(p, f)
