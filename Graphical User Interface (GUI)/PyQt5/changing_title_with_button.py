from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [
    "My Window Title",
    "Still My Window Title",
    "Another Window Title",
    "Still My Another Window Title",
    "Something went wrong!"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_time_clicked = 0

        self.setWindowTitle("My Application")

        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.window_title_changed)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("Button is clicked!")
        self.n_time_clicked += 1
        print(f"Button is clicked {self.n_time_clicked} times!")
        self.button.setText("Click again!")

        window_title = choice(window_titles)
        print(f"Setting the new window title : {window_title}")
        self.setWindowTitle(window_title)

    def window_title_changed(self, window_title):
        print(f"New Window title : {window_title}")

        if window_title == "Something went wrong!":
            self.button.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
