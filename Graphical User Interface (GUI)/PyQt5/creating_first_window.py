from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

import sys


app = QApplication(sys.argv)
# window = QWidget()
window = QMainWindow()
window.setWindowTitle("My First App")
window.setGeometry(120, 150, 300, 300)
window.show()
app.exec_()
