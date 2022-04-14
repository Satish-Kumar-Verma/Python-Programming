

class Father:
    def __init__(self, name):
        self.property = '$120,000,000'
        self.name = name

    def display_property(self):
        print(f"Father's Property : {self.property}")


class Son(Father):
    def __init__(self, name="JJ"):
        super().__init__(name)


s = Son("GG")
print(s.name)
s.display_property()
