from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QProgressBar
import sys
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Q Progress Bar")
        self.setGeometry(100, 100, 500, 500)

        self.btn = QPushButton("Download")
        self.btn.clicked.connect(self.download_now)

        self.progress_bar = QProgressBar()

        layout = QHBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.btn)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def download_now(self):
        for i in range(101):
            time.sleep(0.05)
            self.progress_bar.setValue(i)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
