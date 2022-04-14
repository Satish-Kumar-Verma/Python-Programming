from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit
)
import sys


class Another_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 200, 200)

        self.label = QLabel('Another Window!')
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sending signals from one window to another.")
        self.setGeometry(100, 100, 500, 500)

        self.another_window = Another_Window()

        self.button = QPushButton("Send")
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.another_window.label.setText)

        self.layout_ = QVBoxLayout()
        self.layout_.addWidget(self.button)
        self.layout_.addWidget(self.input)

        container = QWidget()
        container.setLayout(self.layout_)

        self.setCentralWidget(container)

    def toggle_window(self):
        if self.another_window.isVisible():
            self.another_window.hide()

        else:
            self.another_window.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
