from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPalette, QColor
import sys


class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


# app = QApplication(sys.argv)
# color = Color("Green")
# color.show()
# app.exec_()
