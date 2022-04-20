from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.uic import loadUiType
ui, _ = loadUiType("my_window.ui")


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My Window!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
