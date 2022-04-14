from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
import sys
from placeholder_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q VBOX Layout")
        self.setGeometry(100, 100, 300, 300)

        self.layout = QVBoxLayout()
        self.layout.addWidget(Color('Red'))
        self.layout.addWidget(Color('Green'))
        self.layout.addWidget(Color('Blue'))

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
