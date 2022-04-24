

class Person:
    def __init__(self):
        self.name = ""
        self.username = ""
        self.email = ""
        self.phone_number = None
        self.gender = None
        self.dob = None
        self.password = None
        self.address = None
        self.user_type = None

    def set_name(self, name):
        self.name = name

    def set_username(self, uname):
        self.username = uname

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, number):
        self.phone_number = number

    def set_password(self, password):
        self.password = password

    def set_gender(self, gender):
        self.gender = gender

    def set_user_type(self, user_type):
        self.user_type = user_type

    def set_address(self, address):
        self.address = address

    def set_dob(self, date):
        self.dob = date

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob

    def get_address(self):
        return self.address

    def get_user_type(self):
        return self.user_type

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_phone_number(self):
        return self.phone_number
