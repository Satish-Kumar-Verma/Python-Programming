

class Book:
    def __init__(self):
        self.title = None
        self.no_of_pages = None
        self.pub_date = None
        self.author_name = None

    def set_title(self, title):
        self.title = title

    def set_author(self, name):
        self.author_name = name

    def set_no_of_pages(self, nop):
        self.no_of_pages = nop

    def set_pub_date(self, date):
        self.pub_date = date

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author_name

    def get_no_of_pages(self):
        return self.no_of_pages

    def read_book(self):
        return f"Title : {self.title}, \nAuthor : {self.author_name}, \nPublish date : {self.pub_date}"
