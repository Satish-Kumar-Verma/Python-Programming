from PyQt5.QtWidgets import QApplication, QMainWindow, QDial
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q Slider!")
        self.setGeometry(100, 100, 400, 400)

        self.dial = QDial()

        # self.slider.setMinimum(-10)
        # self.slider.setMaximum(3)
        self.dial.setRange(0, 100)
        self.dial.setSingleStep(3)  # arrow from keyboard

        self.dial.valueChanged.connect(self.value_changed)
        self.dial.sliderMoved.connect(self.slider_position)
        self.dial.sliderPressed.connect(self.slider_pressed)
        self.dial.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(self.dial)

    def slider_pressed(self):
        print("Slider is pressed!")

    def slider_released(self):
        print("Slider is released!")

    def value_changed(self, v):
        print(f"Value : {v}")

    def slider_position(self, p):
        print(f"Slider Position : {p}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
