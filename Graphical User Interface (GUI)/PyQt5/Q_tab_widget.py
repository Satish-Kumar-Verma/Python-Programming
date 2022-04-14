from PyQt5.QtWidgets import QApplication, QTabWidget, QMainWindow
import sys
from placeholder_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q Tab Widget")
        self.setGeometry(100, 100, 300, 300)

        self.tab_widget = QTabWidget()
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setTabPosition(QTabWidget.West)
        self.tab_widget.setMovable(True)

        for n, color in enumerate(["Red", "Green", "Blue", "Orange", "Yellow"]):
            self.tab_widget.addTab(Color(color), color)

        # self.tab_widget.addTab(Color("Red"), "Red")
        # self.tab_widget.addTab(Color("Green"), "Green")

        self.setCentralWidget(self.tab_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
