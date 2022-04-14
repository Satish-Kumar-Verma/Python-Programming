from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testing Message Box")
        self.setGeometry(100, 100, 400, 400)
        self.btn = QPushButton("Press me to open a dialog box!")
        self.btn.pressed.connect(self.open_dialog)

        self.setCentralWidget(self.btn)

    def open_dialog(self):
        dialog = QMessageBox.warning(self, "Warning!", "This is a warning!")
        if dialog == QMessageBox.Ok:
            print("Ok is pressed!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
