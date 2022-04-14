from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
import sys


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Child Window")
        self.setGeometry(200, 200, 200, 200)

        layout = QVBoxLayout()
        self.label = QLabel("This is a label on another window!")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.another_window = None
        self.setWindowTitle("Parent Window")
        self.setGeometry(100, 100, 500, 500)

        self.button = QPushButton("Click me to open a new window!")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        if self.another_window is None:
            self.another_window = AnotherWindow()
            self.another_window.show()

        else:
            self.another_window.close()
            self.another_window = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
