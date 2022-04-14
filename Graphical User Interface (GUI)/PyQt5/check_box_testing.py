from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playing with check box.")
        self.setGeometry(100, 200, 400, 400)

        self.check_box = QCheckBox("I agree your terms & conditions.")
        # self.check_box.setCheckState(Qt.Checked)
        self.check_box.setCheckState(Qt.PartiallyChecked)
        # self.check_box.setTristate(True)
        self.check_box.stateChanged.connect(self.check)

        self.setCentralWidget(self.check_box)

    def check(self, state):
        print(state == Qt.Checked)
        print(state)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
