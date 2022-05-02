from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.uic import loadUiType
from PyQt5.QtCore import Qt

ui, _ = loadUiType("calculator.ui")


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.input_text = ""

        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setReadOnly(True)

        self.btn_1.clicked.connect(lambda: self.btn_clicked(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.btn_clicked(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.btn_clicked(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.btn_clicked(self.btn_4))
        self.btn_5.clicked.connect(lambda: self.btn_clicked(self.btn_5))
        self.btn_6.clicked.connect(lambda: self.btn_clicked(self.btn_6))
        self.btn_7.clicked.connect(lambda: self.btn_clicked(self.btn_7))
        self.btn_8.clicked.connect(lambda: self.btn_clicked(self.btn_8))
        self.btn_9.clicked.connect(lambda: self.btn_clicked(self.btn_9))
        self.btn_0.clicked.connect(lambda: self.btn_clicked(self.btn_0))
        self.btn_00.clicked.connect(lambda: self.btn_clicked(self.btn_00))
        self.btn_000.clicked.connect(lambda: self.btn_clicked(self.btn_000))
        self.btn_plus.clicked.connect(lambda: self.btn_clicked(self.btn_plus))
        self.btn_minus.clicked.connect(lambda: self.btn_clicked(self.btn_minus))
        self.btn_mult.clicked.connect(lambda: self.btn_clicked(self.btn_mult))
        self.btn_div.clicked.connect(lambda: self.btn_clicked(self.btn_div))
        self.btn_dot.clicked.connect(lambda: self.btn_clicked(self.btn_dot))
        self.btn_mod.clicked.connect(lambda: self.btn_clicked(self.btn_mod))
        self.btn_cancel.clicked.connect(lambda: self.btn_clicked(self.btn_cancel))
        self.open_bracket.clicked.connect(lambda: self.btn_clicked(self.open_bracket))
        self.closed_bracket.clicked.connect(lambda: self.btn_clicked(self.closed_bracket))

        self.btn_eq.clicked.connect(self.calculate)

    def btn_clicked(self, button):
        if button.text() == " x ":
            self.input_text += " * "

        elif button.text() == "CE":
            self.input_text = ""

        else:
            self.input_text += button.text()

        self.lineEdit.setText(self.input_text)

    def calculate(self):
        try:
            result = str(eval(self.input_text))
        except SyntaxError:
            result = "Error"
        self.lineEdit.setText(result)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
