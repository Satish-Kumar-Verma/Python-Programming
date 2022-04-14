

class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.contact = None
        self.dob = None
        self.username = None
        self.password = None
        self.book_collection = []

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_contact(self, contact):
        self.contact = contact

    def set_dob(self, dob):
        self.dob = dob

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_collection(self):
        return self.book_collection

    def read_book(self, book):
        print(book)
