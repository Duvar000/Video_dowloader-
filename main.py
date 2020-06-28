import os
from PyQt5 import  uic
from PyQt5.QtWidgets import *
from pytube import YouTube

windows = QApplication([])
screen = uic.loadUi("windows.ui")

def Dowload():
    if screen.comboBox.currentText() == "360p":
        try:
            link = screen.lineEdit.text()
            youtube = YouTube(link)
            print(youtube.title , "dowloading...")
            stream = youtube.streams.get_by_itag(18) 
            stream.download("video")
            print("sccussfully!")
        except:
            print("error")
    if screen.comboBox.currentText() == "720p":
        try:
            link = screen.lineEdit.text()
            youtube = YouTube(link)
            print(youtube.title , "dowloading...")
            stream = youtube.streams.get_by_itag(22) 
            stream.download("video")
            print("sccussfully!")
        except:
            print("error")
    if screen.comboBox.currentText() == "mp3":
        try:
            link = screen.lineEdit.text()
            youtube = YouTube(link)
            print(youtube.title , "dowloading...")
            stream = youtube.streams.get_by_itag(251) 
            video = stream.download("video")
            video
            os.rename(video , youtube.title+".mp3")
            print("sccussfully!")
        except:
            print("error")



screen.pushButton.clicked.connect(Dowload)

screen.show()
windows.exec_()

