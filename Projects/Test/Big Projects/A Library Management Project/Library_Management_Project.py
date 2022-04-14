from Library import Library
from Person import Person
import pickle

accounts = []

def refresh():
    try:
        global accounts
        accounts = []
        with open("user_accounts.dat", "rb") as f:
            while True:
                obj = pickle.load(f)
                accounts.append(obj)
    except EOFError:
        pass

def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    for i in range(len(accounts)):
        if accounts[i].get_username() == username and accounts[i].get_password() == password:
            return True, accounts[i]

    else:
        return False

def create_account():
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    dob = input("Enter your DOB : ")
    contact = input("Enter your phone number : ")
    username = input("Enter your username : ")
    password = input("Enter the password : ")

    p = Person()
    p.set_name(name)
    p.set_age(age)
    p.set_dob(dob)
    p.set_contact(contact)
    p.set_username(username)
    p.set_password(password)

    with open("user_accounts.dat", "ab") as f:
        pickle.dump(p, f)
    refresh()
    return p


if __name__ == '__main__':
    with open("user_accounts.dat", "a") as f:
        pass
    lib = Library()
    lib.set_address("Mandalay")

    print(f"Welcome to {lib.get_name()} Library!")
    have_account = input("Do you have an account? [Y/n] : ").lower()
    refresh()
    if have_account == 'y':
        login_status, person = login()
        if not login_status:
            print("You have entered incorrect information. Please try again!")
            exit(-1)

    else:
        person = create_account()

    print("Login success!")

    choice = input("Read/ Add / Borrow / Return")

    if choice.lower() == 'borrow':
        lib.add_book()
        lib.borrow()




