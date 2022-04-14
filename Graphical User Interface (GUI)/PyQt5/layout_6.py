from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout, QStackedWidget
import sys
from placeholder_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q Stacked Layout")
        self.setGeometry(100, 100, 300, 300)

        self.layout = QStackedLayout()
        self.layout.addWidget(Color('Red'))
        self.layout.addWidget(Color('Green'))
        self.layout.addWidget(Color('Blue'))

        self.layout.setCurrentIndex(1)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        # self.widget = QStackedWidget()
        # self.widget.addWidget(Color("Red"))
        # self.widget.addWidget(Color("Green"))
        # self.widget.addWidget(Color("Blue"))
        #
        # self.widget.setCurrentIndex(1)

        self.setCentralWidget(self.widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
