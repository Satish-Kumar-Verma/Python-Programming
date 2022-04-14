import pickle


def write_data(file, obj):
    with open(f"{file}.dat", "ab") as f:
        pickle.dump(obj, f)


def read_data(file):
    data = []
    with open(f"{file}.dat", "rb") as f:
        try:
            while True:
                data.append(pickle.load(f))
        except EOFError:
            pass
    return data


def remove_book(file, obj):
    data = []
    with open(f"{file}.dat", "rb") as f:
        try:
            while True:
                data.append(pickle.load(f))
        except EOFError:
            pass

    for book in data:
        if book.get_title() == obj.get_title():
            data.remove(book)

    with open(f"{file}.dat", "wb") as f:
        for book in data:
            pickle.dump(book, f)


def update_user(obj):
    data = []
    with open("User-accounts.dat", "rb") as f:
        try:
            while True:
                data.append(pickle.load(f))
        except EOFError:
            pass

    for i in range(len(data)):
        if data[i].get_name().lower() == obj.get_name().lower():
            data[i] = obj

    with open("User-accounts.dat", "wb") as f:
        for person in data:
            pickle.dump(person, f)
