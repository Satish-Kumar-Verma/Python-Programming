
class Book:
    def __init__(self, name, author, no_of_pages):
        # instant variables
        self.name = name
        self.author = author
        self.no_of_pages = no_of_pages

    def read(self):
        print(f'Book name : {self.name}, Author = {self.author}')

    # getter methods
    def getNumbPages(self):
        print(f"Book name : {self.name}, No of Pages : {self.no_of_pages}")

    def get_author(self):
        return self.author


b = Book("A", "b", 12)
b.read()
# print(b.get_author())
print(b.author)
