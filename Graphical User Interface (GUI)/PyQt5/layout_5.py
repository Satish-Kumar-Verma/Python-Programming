from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout
)
import sys
from placeholder_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q Grid Layout")

        self.setGeometry(100, 100, 300, 300)

        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(Color("Red"), 0, 0)
        self.layout.addWidget(Color("Green"), 1, 1)
        self.layout.addWidget(Color("Blue"), 2, 2)
        self.layout.addWidget(Color("Blue"), 3, 3)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
