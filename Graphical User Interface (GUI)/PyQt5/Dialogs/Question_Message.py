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

    # def open_dialog(self):
    #     dialog = QMessageBox(self)
    #     dialog.setWindowTitle("I have a question!")
    #     dialog.setText("This is a question dialog!")
    #     dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    #     dialog.setIcon(QMessageBox.Question)
    #     temp = dialog.exec_()
    #     if temp == QMessageBox.Yes:
    #         print("Yes")
    #     else:
    #         print("No")

    def open_dialog(self):
        dialog = QMessageBox.question(self, "This is a Question Box", "This is my question!")
        if dialog == QMessageBox.Yes:
            print("Yes")

        else:
            print("No")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
