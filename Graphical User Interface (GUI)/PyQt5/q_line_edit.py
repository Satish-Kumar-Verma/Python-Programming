from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q Line Edit")
        self.setGeometry(200, 200, 500, 500)

        self.input = QLineEdit()
        self.input.setMaxLength(10)
        self.input.setPlaceholderText("Username")

        self.input.returnPressed.connect(self.on_return_pressed)
        self.input.selectionChanged.connect(self.on_selection_change)
        self.input.textChanged.connect(self.on_text_change)
        self.input.textEdited.connect(self.on_text_edited)

        self.setCentralWidget(self.input)

    def on_return_pressed(self):
        print("Enter key was pressed!")
        self.centralWidget().setText("12345678910")

    def on_selection_change(self):
        print("Selection changed!")
        print(self.centralWidget().selectedText())

    def on_text_change(self, s):
        print("Text Changed!")
        print(s)

    def on_text_edited(self, s):
        print("Text edited!")
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
