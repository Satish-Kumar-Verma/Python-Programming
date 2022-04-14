from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testing Label!")

        self.label = QLabel("Hello!")

        # font = self.label.font()
        # font.setPointSize(100)
        # self.label.setFont(font)
        self.label.setFont(QFont('Bookman Old Style', 200))
        # self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.setCentralWidget(self.label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
