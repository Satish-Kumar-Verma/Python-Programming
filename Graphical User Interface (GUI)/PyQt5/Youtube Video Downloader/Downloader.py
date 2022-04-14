from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QLineEdit,
    QWidget
)
from PyQt5.QtCore import Qt
from pytube import YouTube
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Downloader")
        self.setGeometry(100, 100, 500, 400)
        self.input_text = ""
        self.video_path = "/home/sonu/Desktop"

        self.label = QLabel("La Plu Ma YouTube Video Downloader!")
        self.label.setAlignment(Qt.AlignCenter)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter the link")
        self.input.textChanged.connect(self.input_changed)

        self.download_btn = QPushButton("Download")
        self.download_btn.pressed.connect(self.download_now)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.input)
        self.h_layout.addWidget(self.download_btn)
        self.h_layout.setAlignment(Qt.AlignTop)

        self.v_layout.addLayout(self.h_layout)

        container = QWidget()
        container.setLayout(self.v_layout)

        self.setCentralWidget(container)

    def input_changed(self, text):
        self.input_text = text

    def download_now(self):
        yt = None
        try:
            yt = YouTube(self.input_text)
        except ConnectionError:
            print("Connection Error!")

        try:
            yt.streams.get_highest_resolution().download(self.video_path)

        except Exception:
            print("Download Error!")

        print("Task Completed!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
