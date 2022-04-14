from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q List Widget")
        self.setGeometry(200, 200, 500, 500)

        self.l_widget = QListWidget()
        self.l_widget.addItems(["One", "Two", "Three"])

        self.l_widget.currentItemChanged.connect(self.on_index_change)
        self.l_widget.currentTextChanged.connect(self.on_text_change)

        self.setCentralWidget(self.l_widget)

    def on_index_change(self, i):
        print(i.text())

    def on_text_change(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
