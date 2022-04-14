from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout
import sys


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.d_b_box = QDialogButtonBox(buttons)
        self.d_b_box.accepted.connect(self.accept)
        self.d_b_box.rejected.connect(self.reject)

        self.message = QLabel("Something went wrong!")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.d_b_box)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testing Q Dialogs")

        self.btn = QPushButton("Press me to open a dialog box!")
        self.btn.pressed.connect(self.open_dialog)

        self.setCentralWidget(self.btn)

    def open_dialog(self):
        my_dialog_box = CustomDialog()
        temp = my_dialog_box.exec_()
        if temp:
            print("OK is pressed!")
        else:
            print("Cancel is pressed!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
