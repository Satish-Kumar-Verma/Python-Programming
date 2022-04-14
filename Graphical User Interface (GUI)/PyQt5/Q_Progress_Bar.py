from PyQt5.QtWidgets import QProgressBar, QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q Progress Bar")
        self.setGeometry(100, 100, 400, 400)
        self.btn = QPushButton("Download")
        self.btn.clicked.connect(self.progress)

        self.progress_bar = QProgressBar()

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.progress_bar)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def progress(self):
        for i in range(101):
            time.sleep(0.03)
            self.progress_bar.setValue(i)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
