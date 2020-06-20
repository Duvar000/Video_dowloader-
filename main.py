import os
from PyQt5 import  uic
from PyQt5.QtWidgets import *
from pytube import YouTube

windows = QApplication([])
screen = uic.loadUi("windows.ui")

def Dowload_360p():
    try:
        link = screen.lineEdit.text()
        youtube = YouTube(link)
        print(youtube.title , "dowloading...")
        stream = youtube.streams.get_by_itag(18) 
        stream.download("video")
        print("sccussfully!")
    except:
        print("error")
def Dowload_720p():
    try:
        link = screen.lineEdit.text()
        youtube = YouTube(link)
        print(youtube.title , "dowloading...")
        stream = youtube.streams.get_by_itag(22) 
        stream.download("video")
        print("sccussfully!")
    except:
        print("error")
def dowload_mp3 ():
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



screen.pushButton_1.clicked.connect(dowload_mp3)
screen.pushButton_2.clicked.connect(Dowload_360p)
screen.pushButton_3.clicked.connect(Dowload_720p)

screen.show()
windows.exec_()

