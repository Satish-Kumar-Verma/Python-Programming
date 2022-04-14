
class Person:
    no_of_person = 0  # class variable or static variable

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.no_of_person += 1

    def speak(self):
        print(f"Hi! I am {self.name}. And I can speak!")

    def walk(self):
        print(f"Hi! I am {self.name}. And I can walk!")

    def sleep(self):
        print(f"Hi! I am {self.name}. And I can sleep!")

    @classmethod
    def get_no_of_person(cls):
        return cls.no_of_person

    @staticmethod
    def get_no_of_person_():
        return Person.no_of_person

    def __repr__(self):
        return f"Hi! I am {self.name}. And I am {self.age} years old! See you tomorrow!"

    def __str__(self):
        return f"Hi! I am {self.name}. Hi! And I am {self.age} years old! See you tomorrow!"


p1 = Person("AKM", 22, "female")
p2 = Person("KPP", 40, 'male')

# print(p1.no_of_person)
# print(Person.no_of_person)
# print(p1.get_no_of_person())

print(Person.get_no_of_person_())

# p1.walk()
# p1.speak()
# p2.walk()
# p1.sleep()

# print(p1.age)
# print(p2.name)
# print(p1)
