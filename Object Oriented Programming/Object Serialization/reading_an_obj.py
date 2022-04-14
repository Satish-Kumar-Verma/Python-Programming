import pickle  # Deserialization


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name}. And I am {self.age} years old!"


with open("person_info.dat", "rb") as f:
    person = pickle.load(f)

    print(person)
