from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QWidget
)
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mouse Events")
        self.setGeometry(100, 100, 500, 500)

        self.label = QLabel("Click!")
        self.label_2 = QLabel("Mouse!")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def mouseMoveEvent(self, e):
        self.label_2.setText("Mouse Moved!")
        # print(f"Pointer's coordinate : ({e.x()}, {e.y()})")
        print(f"Pointer's position : {e.pos()}")
        # print(f"Pointer's Position (Global) : {e.globalPos()}")
        # print(f"Global X : {e.globalX()}")

    def mousePressEvent(self, e):
        self.label.setText("Mouse Pressed!")

        if e.button() == Qt.LeftButton:
            print("Left button is pressed!")

        elif e.button() == Qt.RightButton:
            print("Right button is pressed!")

    def mouseReleaseEvent(self, e):
        self.label.setText("Mouse Released!")
        self.label_2.setText("Released!")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("Mouse Double clicked!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
