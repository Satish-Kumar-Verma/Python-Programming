from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QProgressBar, QLineEdit, QLabel
import sys
from pytube import YouTube


class MainWindow(QMainWindow):
    def __init__(self):
        self.link = None
        super().__init__()
        self.setWindowTitle('Download anything!')
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel("Welcome to my video downloader!")

        self.progress_bar = QProgressBar()

        self.download_btn = QPushButton("Download")
        self.download_btn.clicked.connect(self.download_now)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.update_link)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.input)
        self.h_layout.addWidget(self.download_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.progress_bar)

        container = QWidget()
        container.setLayout(self.v_layout)

        self.setCentralWidget(container)

    def update_link(self, text):
        self.link = text

    def handle_progress(self, stream, chunk, bytes_remaining):
        # read_data = block_num * block_size
        # if total_size > 0:
        #     download_percentage = (read_data * 100) / total_size
        #     self.progress_bar.setValue(download_percentage)
        #     QApplication.processEvents()
        print(stream, chunk, bytes_remaining)

    def download_now(self):
        video = YouTube(self.link)
        video.streams.get_highest_resolution().download()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
