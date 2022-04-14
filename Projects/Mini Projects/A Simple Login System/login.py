
#  Do you want to login or create an account [login, create]?
#  login
#  Enter your username :
#  Enter your password :
#  username, password == (username and password) stored in a file after the user account has been created.

#  if the username is not found in the file, your program must prompt that this user account does not exist.
#  if the user account does not exist in the database, your program should ask the user whether he/she wants to
#  create a new account or not (create a new account only if the username does not exist in the database.)

#  or if the username is in the file and either of username and password is incorrect, your program must prompt :
#  "wrong username or password"

#  if the user logged in to the system, your program should prompt "Logged in successfully!"


def get_credentials(data):
    data = list(map(lambda s: s.strip('\n'), data))
    temp = []
    credentials = {}
    for item in data:
        if "Name" not in item:
            temp.append(item)

    for i in range(0, len(temp), 2):
        credentials[temp[i].split(" : ")[1]] = temp[i + 1].split(" : ")[1]
        # temp = {}
        # temp[key] = value
        # temp.update({key:value})
        # temp.setdefault(key, value)
    return credentials


with open("credentials.txt", "a") as f:
    pass

with open("credentials.txt", "r") as file:
    data = file.readlines()

credentials = get_credentials(data)

def create_account():
    name = input("Enter your full name : ")
    username = input("Enter your username : ")
    password = input("Enter the password : ")

    if username not in credentials.keys():
        with open("credentials.txt", "a+") as f:
            f.write(f"Name : {name}\nusername : {username}\npassword : {password}\n")

def login():
    username = input("Enter your username : ")
    password = input("Enter the password : ")

    if username not in credentials.keys():
        print("Your username doesn't exist in our system!")
        choice = input("Do you want to create an account? [Y/n] : ")
        if choice.lower() == 'y':
            create_account()
        else:
            print("Why are you gay?!")
            print("BYE! You GAYYY!")
    else:
        if password == credentials[username]:
            print("You have logged in to our system successfully!")

        else:
            print("Wrong username or password!")


if __name__ == '__main__':
    choice = input("Do you want to login or create an account [login/create] : ")
    if choice.lower() == 'login':
        login()

    elif choice.lower() == 'create':
        create_account()

    else:
        print("Wrong choice!")

