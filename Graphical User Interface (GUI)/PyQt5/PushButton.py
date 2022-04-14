from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from playsound import playsound
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("Push Button")
        # self.setFixedSize(QSize(400, 300))

        self.button = QPushButton("Play Music")
        self.button.setCheckable(True)
        # button.setDisabled(True)
        # button.setDisabled(False)
        self.button.clicked.connect(self.button_clicked)
        # self.button.clicked.connect(self.button_is_released)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        # playsound("Titanic - My Heart Will Go On (192  kbps).mp3")
        self.button.setText("You have already clicked me!")
        self.button.setEnabled(False)
        self.setWindowTitle("My One Shot App")

    def button_toggled(self, checked):
        self.button_is_checked = checked

    def button_is_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
