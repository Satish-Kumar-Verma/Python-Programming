from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testing Message Box")

        self.btn = QPushButton("Press me to open a dialog box!")
        self.btn.pressed.connect(self.open_dialog)

        self.setCentralWidget(self.btn)

    def open_dialog(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("I have a question!")
        dialog.setText("This is a simple dialog!")
        temp = dialog.exec_()

        if temp == QMessageBox.Ok:
            print("OK is pressed!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
