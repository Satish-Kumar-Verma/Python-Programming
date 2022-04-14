from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QAction, QStatusBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q Toolbar")
        self.setGeometry(100, 100, 500, 500)

        self.label = QLabel("Hello")
        self.label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.label)

        self.toolbar = QToolBar("My Toolbar")
        self.addToolBar(self.toolbar)

        self.action_btn = QAction(QIcon("./Icons/icons/book.png"), "My Button", self)
        self.action_btn.setStatusTip("This is my action button!")
        self.action_btn.setCheckable(True)
        self.action_btn.triggered.connect(self.onMyToolBarButtonClick)
        self.toolbar.addAction(self.action_btn)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("Clicked", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
