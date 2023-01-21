import tkinter
import customtkinter as CTk
from pytube import YouTube
import json


def download_highest_res():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(
            text="Youtube link is invalid.", text_color="red")


def download_lowest_res():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_lowest_resolution()
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(
            text="Youtube link is invalid.", text_color="red")


def download_720p():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_by_resolution("720p")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(
            text="Youtube link is invalid.", text_color="red")


def audio_only():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(
            text="Youtube link is invalid.", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size ^ bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    progressPercent.configure(text=per + '%')
    progressPercent.update()
    progressBar.set(float(percentage_of_compeletion)/100)


CTk.set_appearance_mode("System")
CTk.set_default_color_theme("blue")

with open("settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']

if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

app = CTk.CTk()
app.geometry("320x320")
app.title("YouTube Downloader")
app.resizable(False, False)
title = CTk.CTkLabel(
    app, text="Please insert a YouTube link below:")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()

link = CTk.CTkEntry(
    app, width=230, height=40, textvariable=url_var)
link.pack()

finishLabel = CTk.CTkLabel(app, text="")
finishLabel.pack()

progressPercent = CTk.CTkLabel(app, text="0%")
progressPercent.pack()

progressBar = CTk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download_highest_res_button = CTk.CTkButton(
    app, text="Highest Res Download", command=download_highest_res)
download_highest_res_button.place(x=13, y=229)
lowest_res_button = CTk.CTkButton(
    app, text="Lowest Res Download", command=download_lowest_res)
lowest_res_button.place(x=169, y=229)
download_in_720p = CTk.CTkButton(
    app, text="Download in 720p60p", command=download_720p)
download_in_720p.place(x=13, y=270)
audio_only_button = CTk.CTkButton(app,
                                  text="Audio Only", command=audio_only)
audio_only_button.place(x=169, y=270)
app.mainloop()
