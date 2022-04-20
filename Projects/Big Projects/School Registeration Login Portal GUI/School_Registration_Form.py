from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.uic import loadUiType

ui, _ = loadUiType("login_form.ui")


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("School Registration Form")
        self.show()

        logo_pixmap = QPixmap("registration_logo.png")
        self.label.setPixmap(logo_pixmap)
        self.label.setScaledContents(True)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
