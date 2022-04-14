from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton
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

        self.setWindowTitle("Showing and hiding windows!")
        self.setGeometry(100, 100, 500, 500)

        self.another_window = AnotherWindow()

        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self):
        if self.another_window.isVisible():
            self.another_window.hide()

        else:
            self.another_window.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
