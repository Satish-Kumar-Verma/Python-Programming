from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Context Menu!")
        self.setGeometry(100, 100, 400, 400)

    def contextMenuEvent(self, e):
        menu = QMenu()
        action_button1 = QAction("Copy", self)
        action_button1.triggered.connect(self.testing)
        menu.addAction(action_button1)
        menu.addAction(QAction("Cut", self))
        menu.addAction(QAction("Paste", self))
        menu.exec_(e.globalPos())

    def testing(self):
        print("Copied!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
