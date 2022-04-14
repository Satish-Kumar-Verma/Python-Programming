from book import Book

class Library:
    available_books = []
    borrowed_books = []
    def __init__(self):
        self.name = "La Pluu Ma"
        self.address = None

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def borrow(self):
        book_name = input("Enter the book name : ")
        for i in range(len(Library.available_books)):
            if Library.available_books[i].get_title() == book_name:
                print("You may borrow the book!")
                Library.borrowed_books.append(Library.available_books[i])
                Library.available_books.remove(Library.available_books[i])
                break

        else:
            print("Sorry! The book is not available in the library!")

    def return_book(self):
        book_name = input("Enter the book name : ")
        for i in range(len(Library.borrowed_books)):
            if Library.borrowed_books[i].get_title() == book_name:
                print("You may return the book!")
                Library.available_books.append(Library.borrowed_books[i])
                Library.borrowed_books.remove(Library.borrowed_books[i])
                break

        else:
            print("Something wrong! Please Try again!")

    def add_book(self):
        book_name = input("Enter the book name : ")
        author_name = input("Enter the author name : ")
        no_of_pages = input("Enter the no of pages : ")
        pub_date = input("Enter the published date : ")

        b = Book()
        b.set_author(author_name)
        b.set_title(book_name)
        b.set_no_of_pages(no_of_pages)
        b.set_pub_date(pub_date)
        Library.available_books.append(b)


