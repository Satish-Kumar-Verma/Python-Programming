

class Father:
    def height(self):
        print("6 feet 2 inches!")


class Monther:

    def color(self):
        print("Color is brown!")


class Child(Father, Monther):
    pass

c = Child()
c.height()
c.color()