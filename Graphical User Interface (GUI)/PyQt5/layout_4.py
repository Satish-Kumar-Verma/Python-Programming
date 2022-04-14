from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
import sys
from placeholder_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q VBOX Layout")
        self.setGeometry(100, 100, 300, 300)

        self.layout1 = QHBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout3 = QVBoxLayout()

        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.setSpacing(0)

        self.layout2.addWidget(Color("Red"))
        self.layout2.addWidget(Color("Green"))
        self.layout2.addWidget(Color("Blue"))

        self.layout1.addLayout(self.layout2)
        self.layout1.addWidget(Color("Purple"))

        self.layout3.addWidget(Color("Blue"))
        self.layout3.addWidget(Color("Indigo"))

        self.layout1.addLayout(self.layout3)

        self.widget = QWidget()
        self.widget.setLayout(self.layout1)
        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
