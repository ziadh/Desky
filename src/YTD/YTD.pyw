import tkinter
import customtkinter as CTk
from pytube import YouTube
import json
import subprocess

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

def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"], creationflags=subprocess.CREATE_NO_WINDOW)

CTk.set_appearance_mode("System")
CTk.set_default_color_theme("blue")

with open("src/settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']
version = settings['version']

if theme == 'Dark':
    CTk.set_appearance_mode("Dark")
else:
    CTk.set_appearance_mode("Light")

app = CTk.CTk()
app.geometry("320x320")
app.title(f"YouTube Downloader v{version}")
app.wm_iconbitmap("assets/logos/yd-logo.ico")

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
download_highest_res_button.place(x=13, y=189)
lowest_res_button = CTk.CTkButton(
    app, text="Lowest Res Download", command=download_lowest_res)
lowest_res_button.place(x=169, y=189)
download_in_720p = CTk.CTkButton(
    app, text="Download in 720p60p", command=download_720p)
download_in_720p.place(x=13, y=230)
audio_only_button = CTk.CTkButton(app,
                                  text="Audio Only", command=audio_only)
audio_only_button.place(x=169, y=230)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=13, y=271)

exit_button = CTk.CTkButton(
    app, text="Exit", command=exit)
exit_button.place(x=169, y=271)
app.mainloop()
