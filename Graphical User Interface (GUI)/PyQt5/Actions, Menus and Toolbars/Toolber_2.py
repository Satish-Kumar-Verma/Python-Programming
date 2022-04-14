from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QLabel, QCheckBox, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbar with seperator!")
        self.setGeometry(100, 100, 300, 300)

        self.label = QLabel("Hello")
        self.label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.label)

        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(16, 16))
        self.toolbar.setFixedHeight(40)
        self.addToolBar(self.toolbar)

        self.action_btn1 = QAction(QIcon("./Icons/icons/bug.png"), "Button 1", self)
        self.action_btn1.setStatusTip("This is button 1.")
        self.action_btn1.triggered.connect(self.onMyActionButtonClick)
        self.action_btn1.setCheckable(True)
        self.toolbar.addAction(self.action_btn1)

        self.toolbar.addSeparator()

        self.action_btn2 = QAction(QIcon("./Icons/icons/bluetooth.png"), "Button 2", self)
        self.action_btn2.setStatusTip("This is button 2.")
        self.action_btn2.triggered.connect(self.onMyActionButtonClick)
        self.action_btn2.setCheckable(True)
        self.toolbar.addAction(self.action_btn2)

        self.setStatusBar(QStatusBar(self))

        self.toolbar.addWidget(QLabel("Hello"))
        self.toolbar.addWidget(QCheckBox())

    def onMyActionButtonClick(self, s):
        print(f"Clicked {s}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
