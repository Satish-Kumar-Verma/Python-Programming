from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A weird cat")
        self.setGeometry(200, 100, 600, 600)

        self.label = QLabel()
        pix_obj = QPixmap("cat.jpeg")
        # pix_obj = pix_obj.scaledToWidth(500)
        # pix_obj = pix_obj.scaledToHeight(500)
        self.label.setPixmap(pix_obj)
        self.label.setScaledContents(True)

        self.setCentralWidget(self.label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
