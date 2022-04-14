from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q List Widget")
        # self.setGeometry(200, 200, 500, 500)

        self.s_box = QSpinBox()
        self.s_box.setMinimum(-10)
        self.s_box.setMaximum(5)
        self.s_box.setSingleStep(1)
        self.s_box.setPrefix("$")
        self.s_box.setSuffix("c")

        self.s_box.textChanged.connect(self.on_text_change)
        self.s_box.valueChanged.connect(self.on_value_change)

        self.setCentralWidget(self.s_box)

    def on_value_change(self, v):
        print(f"Value = {v}")

    def on_text_change(self, s):
        print(f"Text = {s}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
