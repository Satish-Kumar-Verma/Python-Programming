# Public - accessible from anywhere e.g. self.name
# Protected - accessible from the same package e.g. self._name
# Private - accessible only in the class e.g. self.__name


class Book:
    def __init__(self):
        # instant variables
        self.name = None
        self.author = None
        self.no_of_pages = None

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_no_of_pages(self, no_of_pages):
        self.no_of_pages = no_of_pages

    # Getter methods

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_no_of_pages(self):
        return self.no_of_pages

    def __str__(self):
        return f"Book Name : {self.name} \nAuthor Name : {self.author}"


book = Book()

book.set_name("Core Python Programming")
book.set_author("N. G. Rao")
book.set_no_of_pages(23)
# print(book.get_name())
# print(book.get_author())
# print(book.get_no_of_pages())
print(book)
