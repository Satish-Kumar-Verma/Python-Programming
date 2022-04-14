

class Book:
    def __init__(self, title, author, publish_date, pages):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.pages = pages

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_date(self, publish_date):
        self.publish_date = publish_date

    def set_no_of_page(self, page):
        self.pages = page

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_date(self):
        return self.publish_date

    def get_page(self):
        return self.pages

    def read(self):
        return f"{self.title} written by {self.author} \nPublished on {self.publish_date} \nNo. of pages : {self.pages}"

    def __str__(self):
        return f"{self.title} written by {self.author} \nPublished on {self.publish_date} \nNo. of pages : {self.pages}"
