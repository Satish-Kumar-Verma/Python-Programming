from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Playing with Combo box!")

        self.setGeometry(200, 100, 500, 500)

        self.c_box = QComboBox()
        self.c_box.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.c_box.addItems(["One", "Two", "Three"])

        self.c_box.setEditable(True)
        self.c_box.addItem("Four")
        self.c_box.addItem("Five")
        # self.c_box.setMaxCount(5)

        self.c_box.currentIndexChanged.connect(self.index_changed)
        # self.c_box.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(self.c_box)

    def index_changed(self, i):
        print(i)

    def text_changed(self, text):
        print(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
