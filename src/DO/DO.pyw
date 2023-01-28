from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
import os
import shutil
import customtkinter as CTk
import json
import subprocess

downloads_path = ''


def set_path():
    global downloads_path
    downloads_path = tkinter.filedialog.askdirectory()


def help_function():
    message = messagebox.showinfo(
        title="Help", message="This program organizes your Downloads folder into seperate folders. Each folder containing all files from a certain file type (e.g. Downloaded Videos, Downloaded Images,etc.)")


def organize():
    global downloads_path
    if downloads_path == '':
        error_label.configure(text="Please set your downloads folder first.")
    else:
        error_label.configure(text="")
        os.makedirs(downloads_path+"/Downloaded Images", exist_ok=True)
        os.makedirs(downloads_path+"/Downloaded Videos", exist_ok=True)
        os.makedirs(downloads_path+"/Downloaded PDFs", exist_ok=True)
        os.makedirs(downloads_path+"/Downloaded ZIPs", exist_ok=True)
        os.makedirs(downloads_path+"/Downloaded Docs", exist_ok=True)

        file_types = {
            "jpg": "Downloaded Images",
            "jpeg": "Downloaded Images",
            "png": "Downloaded Images",
            "gif": "Downloaded Images",
            "mp4": "Downloaded Videos",
            "pdf": "Downloaded PDFs",
            "zip": "Downloaded ZIPs",
            "rar": "Downloaded ZIPs",
            "doc": "Downloaded Docs",
            "docx": "Downloaded Docs"
        }
        for file_name in os.listdir(downloads_path):
            file_ext = file_name.split(".")[-1].lower()
            if file_ext in file_types:
                shutil.move(downloads_path+"/"+file_name,
                            downloads_path+"/"+file_types[file_ext]+"/"+file_name)
        error_label.configure(text="Download folder organized successfully!")


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


with open("settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']


app = CTk.CTk()
CTk.set_default_color_theme("blue")
if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.resizable(False, False)
app.geometry(f"290x200")
app.title("Downloads Organizer")
app.wm_iconbitmap("src/DO/logo.ico")

welcome_label = CTk.CTkLabel(
    app, text="Welcome to Downloads Organizer!")

welcome_label.place(x=10, y=0)

locate_button = CTk.CTkButton(
    app, text="Set Downloads Folder", command=set_path, width=20)

organize_button = CTk.CTkButton(
    app, text="Organize", width=10, command=organize)

help_button = CTk.CTkButton(
    app, text="How Does This Work", width=15, command=help_function)
exit_button = CTk.CTkButton(app, text="Exit", width=65, command=exit)
error_label = CTk.CTkLabel(app, text="")

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=60, y=155)

error_label.place(x=10, y=35)

locate_button.place(x=10, y=76)
organize_button.place(x=180, y=76)
help_button.place(x=10, y=115)
exit_button.place(x=180, y=115)
app.mainloop()
