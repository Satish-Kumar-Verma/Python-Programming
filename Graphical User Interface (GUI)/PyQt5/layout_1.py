from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
import sys
from placeholder_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Colors")

        widget = Color("Green")

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
