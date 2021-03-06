from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUiType
import sys
from pytube import YouTube
import requests

ui, _ = loadUiType("Downloader.ui")


class ProgressDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Downloading")

        self.V_layout = QVBoxLayout()

        self.video_title = QLabel()

        self.download_progress = QProgressBar()

        self.downloaded_size = QLabel()

        self.V_layout.addWidget(self.video_title)
        self.V_layout.addWidget(self.download_progress)
        self.V_layout.addWidget(self.downloaded_size)
        self.setLayout(self.V_layout)


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Downloader")
        self.yt_video = None
        self.videos = None
        self.best_res_size = None

        self.pushButton.clicked.connect(self.search)

        self.comboBox.currentIndexChanged.connect(self.change_size)
        self.pushButton_2.clicked.connect(self.download_now)

    def change_size(self, index):
        if index != 3:
            size = self.videos[index].filesize / (1024 * 1024)
            self.label_7.setText(f"{size:.2f} MB")

        else:
            best_res_size = self.yt_video.streams.get_highest_resolution().filesize
            best_res_size = best_res_size / (1024 * 1024)
            label_text = f"{best_res_size:.2f} MB"
            self.label_7.setText(label_text)

    def on_download_complete(self):
        dialog_box = QMessageBox.information(self, "Congratulations", "Video is downloaded successfully!")
        if dialog_box == QMessageBox.Ok:
            pass

    def download_now(self):
        if self.comboBox.currentText() == "Best Resolution":
            self.yt_video.streams.get_highest_resolution().download()
            self.on_download_complete()
        else:
            self.videos[self.comboBox.currentIndex()].download()
            self.on_download_complete()
            progress = ProgressDialog()
            progress.show()

    def search(self):
        link = self.lineEdit.text()
        self.yt_video = YouTube(link)
        self.videos = self.yt_video.streams.filter(progressive=True)
        self.label_5.setText(f"{self.yt_video.title}")
        img_url = self.yt_video.thumbnail_url
        response = requests.get(img_url)
        with open("thumbnail.png", "wb") as file:
            file.write(response.content)
        self.label_2.setPixmap(QPixmap("thumbnail.png"))
        self.label_8.setText(f"{self.yt_video.length // 60}:{self.yt_video.length % 60}")
        self.comboBox.clear()
        for video in self.videos:
            self.comboBox.addItem(video.resolution)

        self.comboBox.addItem("Best Resolution")
        self.comboBox.setCurrentIndex(3)
        best_res_size = self.yt_video.streams.get_highest_resolution().filesize
        best_res_size = best_res_size / (1024 * 1024)
        label_ = f"{best_res_size:.2f} MB"
        self.label_7.setText(label_)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
