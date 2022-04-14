
# what do you want to do? [borrow, read, return a book]
# book_info file : store the information about the books which are available in the library
# borrowed_file : store the information about the borrowed books
# [[Python, N.G.R], [Life of a pie, anonymous]]

# Read: check for the availability
# if available, then read it.
# if not, then ask if he/she wants to read other book

# Borrow
# if available, you can borrow it [Don't forget to ask the name of the person who borrowed the book.]
# if not, print It is not available. Do you want to read other book?

# Return
# Ask for his/her name
# Return the book to the library [...]
#

def read_data(file):
    with open(file, 'a+') as f:
        f.seek(0, 0)
        raw_data = f.readlines()
        raw_data = list(map(lambda x: x.strip('\n'), raw_data))

    data = []
    for item in raw_data:
        data.append(item.split(" : "))
    return data


def write_data(file, data, mode):
    with open(file, mode) as f:
        f.write(f"{data}\n")


def remove_data(file, data):
    all_data = read_data(file)
    for data_ in all_data:
        if data[0] == data_[0]:
            all_data.remove(data_)

    with open(file, 'w') as f:
        pass

    for data_ in all_data:
        data_ = " : ".join(data_)
        write_data(file, data_, 'a')


choice = input("What do you want to do? [borrow, read or return] : ")
available_books = read_data('library.txt')
if choice.lower() == 'borrow':
    borrowed_book = input("Enter the book name : ")
    for book in available_books:
        if borrowed_book in book:
            print("You may borrow the book!")
            name = input("Please tell us your name : ")
            data = " : ".join(book)
            data += " : " + name
            write_data('borrowed_books.txt', data, 'a')
            remove_data('library.txt', book)
            break
    else:
        print("The book is currently not available in the library!")

elif choice.lower() == 'read':
    read_book = input("Enter the book name : ")
    for book in available_books:
        if read_book in book:
            print("You may read the book!")
            print(book)
            break
    else:
        print("The book is currently not available in the library!")

elif choice.lower() == 'return':
    borrowed_books = read_data('borrowed_books.txt')
    return_book = input("Enter the book name : ")
    for book in borrowed_books:
        if return_book in book:
            name = input("Please enter your name : ")
            if name in book:
                print("You may return the book!")
                book.remove(name)
                data = " : ".join(book)
                write_data("library.txt", data, 'a')
                remove_data('borrowed_books.txt', book)
                print("You have successfully returned the book!")
                break
    else:
        print("Something is wrong! Please try again!")
