

class Library:
    def __init__(self):
        self.name = None
        self.open_time = None
        self.close_time = None
        self.no_of_books = None
        self.address = None

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_opening_time(self, time):
        self.open_time = time

    def set_closing_time(self, time):
        self.close_time = time

    def set_no_of_books(self, books):
        self.no_of_books = books

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_opening_time(self):
        return self.open_time

    def get_closing_time(self):
        return self.close_time

    def get_no_of_books(self):
        return self.no_of_books

    def borrow_book(self):
        print("You have borrowed a book successfully!")

    def return_book(self):
        print("You have returned a book successfully!")


lib = Library()
lib.set_name("HI")
print(lib.get_name())
