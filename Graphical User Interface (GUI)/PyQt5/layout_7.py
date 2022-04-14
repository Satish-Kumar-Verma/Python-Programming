from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QStackedLayout
)
import sys
from placeholder_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Changing colors with buttons")
        self.setGeometry(100, 100, 400, 250)

        self.vbox_layout = QVBoxLayout()
        self.hbox_layout = QHBoxLayout()
        self.stacked_layout = QStackedLayout()

        self.stacked_layout.addWidget(Color("Red"))
        self.stacked_layout.addWidget(Color("Green"))
        self.stacked_layout.addWidget(Color("Blue"))

        self.red_button = QPushButton("Red")
        self.red_button.pressed.connect(self.red_pressed)

        self.green_button = QPushButton("Green")
        self.green_button.pressed.connect(self.green_pressed)

        self.blue_button = QPushButton("Blue")
        self.blue_button.pressed.connect(self.blue_pressed)

        self.hbox_layout.addWidget(self.red_button)
        self.hbox_layout.addWidget(self.green_button)
        self.hbox_layout.addWidget(self.blue_button)

        self.vbox_layout.addLayout(self.hbox_layout)
        self.vbox_layout.addLayout(self.stacked_layout)

        self.container = QWidget()
        self.container.setLayout(self.vbox_layout)
        self.setCentralWidget(self.container)

    def red_pressed(self):
        self.stacked_layout.setCurrentIndex(0)

    def green_pressed(self):
        self.stacked_layout.setCurrentIndex(1)

    def blue_pressed(self):
        self.stacked_layout.setCurrentIndex(2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
