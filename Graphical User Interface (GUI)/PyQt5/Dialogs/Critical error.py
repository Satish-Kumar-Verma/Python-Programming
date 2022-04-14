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
        dialog = QMessageBox.critical(self, "Critical Alert!",
                                      "There is an error in your program",
                                      buttons=QMessageBox.Discard |
                                      QMessageBox.NoToAll | QMessageBox.Ignore,
                                      defaultButton=QMessageBox.Discard)
        if dialog == QMessageBox.Discard:
            print("Discard")

        elif dialog == QMessageBox.Ignore:
            print("Ignore")

        elif dialog == QMessageBox.NoToAll:
            print("No To All")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
