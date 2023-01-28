import webbrowser
from tkinter import *
import customtkinter as CTk
from tkinter import messagebox
import subprocess
import json
CTk.set_appearance_mode("Dark")
CTk.set_default_color_theme("blue")


def open_downloads():
    vars_list = [var1.get(), var2.get(), var3.get(), var4.get(),
                 var5.get(), var6.get(), var7.get(), var8.get(), var9.get(), var10.get(), var11.get()]
    if not any(var == 1 for var in vars_list):
        result = messagebox.showinfo(
            title="Nothing selected", message="Please select at least one.")
    else:
        if var1.get() == 1:
            webbrowser.open("https://www.spotify.com/us/download/")
        if var2.get() == 1:
            webbrowser.open("https://www.google.com/chrome/")
        if var3.get() == 1:
            webbrowser.open(
                "https://www.mozilla.org/en-US/firefox/new/")
        if var4.get() == 1:
            webbrowser.open("https://discord.com/download")
        if var5.get() == 1:
            webbrowser.open("https://code.visualstudio.com/download")
        if var6.get() == 1:
            webbrowser.open("https://desktop.github.com/")
        if var7.get() == 1:
            webbrowser.open("https://notepad-plus-plus.org/downloads/")
        if var8.get() == 1:
            webbrowser.open("https://www.skype.com/en/get-skype/")
        if var9.get() == 1:
            # var 9 = steam, 10=evernote, 11=itunes
            webbrowser.open("https://store.steampowered.com/about/")
        if var10.get() == 1:
            webbrowser.open("https://evernote.com/download")
        if var11.get() == 1:
            webbrowser.open("https://support.apple.com/downloads/itunes")
        reset_selections()


def reset_selections():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)


def select_all():
    var1.set(1)
    var2.set(1)
    var3.set(1)
    var4.set(1)
    var5.set(1)
    var6.set(1)
    var7.set(1)
    var8.set(1)
    var9.set(1)
    var10.set(1)
    var11.set(1)

def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"], creationflags=subprocess.CREATE_NO_WINDOW)

app = CTk.CTk()
app.title("Fresh Desktop Checklist")
app.geometry("450x440")
app.resizable(False, False)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()


with open("settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']

if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")


chrome = CTk.CTkCheckBox(app, text="Chrome", variable=var2)
evernote = CTk.CTkCheckBox(app, text="Evernote", variable=var10)
discord = CTk.CTkCheckBox(app, text="Discord", variable=var4)
firefox = CTk.CTkCheckBox(app, text="Firefox", variable=var3)
itunes = CTk.CTkCheckBox(app, text="iTunes", variable=var11)
ghd = CTk.CTkCheckBox(app, text="GitHub Desktop", variable=var6)
np = CTk.CTkCheckBox(app, text="NotePad++", variable=var7)
skype = CTk.CTkCheckBox(app, text="Skype", variable=var8)
spotify = CTk.CTkCheckBox(app, text="Spotify", variable=var1)
steam = CTk.CTkCheckBox(app, text="Steam", variable=var9)
vs = CTk.CTkCheckBox(app, text="VS Code", variable=var5)


chrome.place(x=120, y=110)
evernote.place(x=120, y=140)
discord.place(x=120, y=170)
firefox.place(x=120, y=200)
ghd.place(x=120, y=230)
itunes.place(x=120, y=260)
np.place(x=270, y=110)
skype.place(x=270, y=140)
spotify.place(x=270, y=170)
steam.place(x=270, y=200)
vs.place(x=270, y=230)
msg = """
Welcome to Fresh Desktop Downloads. If your computer recently got through\na factory reset, simply check the boxes for the applications that you would like\nto install then press the download button.
"""
welcome_label = CTk.CTkLabel(
    app, text=msg, justify=LEFT, padx=10, pady=10)
welcome_label.grid(row=0, column=0)

select_all_button = CTk.CTkButton(
    app, text="Select All", command=select_all)
select_all_button.place(x=70, y=312)

clear_selection_button = CTk.CTkButton(
    app, text="Clear Selection", command=reset_selections)
clear_selection_button.place(x=250, y=312)

download_button = CTk.CTkButton(
    app, text="Download", command=open_downloads)
download_button.place(x=70, y=360)

exit_button = CTk.CTkButton(app, text="Exit", command=exit)
exit_button.place(x=250, y=360)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=160, y=401)

app.mainloop()
