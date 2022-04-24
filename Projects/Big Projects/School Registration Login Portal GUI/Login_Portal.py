from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.uic import loadUiType
import pickle

ui, _ = loadUiType("login_form.ui")


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Login Form")

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(sys.exit)

    def login(self):
        username = self.lineEdit_2.text()
        password = self.lineEdit.text()
        print(f"Username : {username}, Password : {password}")
        accounts = []

        with open("Accounts.dat", "rb") as file:
            try:
                while True:
                    obj = pickle.load(file)
                    accounts.append(obj)

            except EOFError:
                pass

        for account in accounts:
            if account.get_username() == username and account.get_password() == password:
                self.label_4.setText("Login Successful!")

            else:
                self.label_4.setText("Wrong credentials!")


app = QApplication(sys.argv)
login_window = MainWindow()
login_window.show()
app.exec_()
