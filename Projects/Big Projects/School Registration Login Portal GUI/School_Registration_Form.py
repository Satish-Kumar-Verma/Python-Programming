from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.uic import loadUiType
from Person import Person
import pickle

ui, _ = loadUiType("Registration_form.ui")


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.curr_password = ""
        self.setupUi(self)
        self.setWindowTitle("School Registration Form")
        self.show()

        logo_pixmap = QPixmap("registration_logo.png")
        self.label.setPixmap(logo_pixmap)
        self.label.setScaledContents(True)

        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(sys.exit)

    def register(self):
        user = Person()
        user.set_name(self.lineEdit_9.text())
        user.set_username(self.lineEdit_10.text())
        user.set_user_type(self.comboBox_2.currentText())
        user.set_gender(self.comboBox.currentText())
        user.set_dob(self.lineEdit_5.text())
        user.set_address(self.lineEdit_3.text())
        user.set_password(self.lineEdit_4.text())
        user.set_phone_number(self.lineEdit_7.text())
        user.set_email(self.lineEdit_8.text())

        print("Logging info to the file!")

        with open("Accounts.dat", "ab") as file:
            pickle.dump(user, file)

        self.info_message()

    def info_message(self):
        message = QMessageBox.information(self, "Information", "Logging successful!")
        if message == QMessageBox.Ok:
            pass


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
