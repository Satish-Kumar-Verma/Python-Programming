import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Application")
        self.setGeometry(100, 300, 300, 200)  # x , y, width, height


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
