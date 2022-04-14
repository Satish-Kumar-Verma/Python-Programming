from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sys

# To convert .ui file to .py file:
# pyuic5 -x {main_window.ui} -o {main_window_.py}

app = QApplication(sys.argv)
window = uic.loadUi("main_window.ui")
window.show()
app.exec_()
