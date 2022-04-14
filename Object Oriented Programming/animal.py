

class Animal:
    no_of_animals = 0

    def __init__(self):
        self.name = "None"
        self.weight = "None"
        self.height = "None"
        self.color = "None"
        Animal.no_of_animals += 1

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color

    def set_weight(self, w):
        self.weight = w

    @classmethod
    def get_no_of_animals(cls):
        return cls.no_of_animals

    def __str__(self):
        return f"Hi! I am a {self.name}.\nColor = {self.color}\nweight = {self.weight}\nheight = {self.height}"


a = Animal()
a1 = Animal()
a.set_name("Lion")
a.set_color("black")
a.set_weight("280 lb")
a.height = "3'"
print(a)
print(f"Total no. of animal objects : {Animal.no_of_animals}")
