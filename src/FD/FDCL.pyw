import webbrowser
from tkinter import *
import customtkinter as CTk
from tkinter import messagebox
import subprocess
import json


CTk.set_appearance_mode("Dark")
CTk.set_default_color_theme("blue")


def open_downloads():
    vars_list = [var0.get(), var1.get(), var2.get(), var3.get(), var4.get(),
                 var5.get(), var6.get(), var7.get(), var8.get(), var9.get(), var10.get(), var11.get()]
    if not any(var == 1 for var in vars_list):
        result = messagebox.showinfo(
            title="Nothing selected", message="Please select at least one.")
    else:
        if var0.get() == 1:
            webbrowser.open(
                "https://www.blizzard.com/en-us/apps/battle.net/desktop")
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
            webbrowser.open("https://store.steampowered.com/about/")
        if var10.get() == 1:
            webbrowser.open("https://evernote.com/download")
        if var11.get() == 1:
            webbrowser.open("https://support.apple.com/downloads/itunes")
        reset_selections()


def reset_selections():
    var0.set(0)
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
    var0.set(1)
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
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)

#FIXME: Finish this function
def download_it_for_me():
    pass


with open("settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']
version = settings['version']


app = CTk.CTk()
app.title(f"Fresh Desktop Checklist v{version}")
app.wm_iconbitmap("assets/logos/FDCL-logo.ico")

app.geometry("600x540")
app.resizable(False, False)
var0 = IntVar()
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


if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

BattleNet = CTk.CTkCheckBox(app, text="BattleNet", variable=var0)
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

BattleNet.place(x=40, y=90)
chrome.place(x=40, y=120)
evernote.place(x=40, y=150)
discord.place(x=170, y=90)
firefox.place(x=170, y=120)
ghd.place(x=170, y=150)
itunes.place(x=300, y=90)
np.place(x=300, y=120)
skype.place(x=300, y=150)
spotify.place(x=430, y=90)
steam.place(x=430, y=120)
vs.place(x=430, y=150)
msg = """
Welcome to Fresh Desktop Downloads. If your computer recently got through a factory reset, simply \ncheck the boxes for the applications that you would like to install then press the download button.
"""
welcome_label = CTk.CTkLabel(
    app, text=msg, justify=LEFT, padx=10, pady=10)
welcome_label.grid(row=0, column=0)

select_all_button = CTk.CTkButton(
    app, text="Select All", command=select_all)
select_all_button.place(x=40, y=212)

clear_selection_button = CTk.CTkButton(
    app, text="Clear Selection", command=reset_selections)
clear_selection_button.place(x=200, y=212)

download_button = CTk.CTkButton(
    app, text="Download", command=open_downloads)
download_button.place(x=360, y=212)

or_text_label = CTk.CTkLabel(app, text='Or')
or_text_label.place(x=320, y=250)

download_it_for_me_label = CTk.CTkLabel(app, text='Download them for me: ')
download_it_for_me_label.place(x=20, y=280)

choose_os_label = CTk.CTkLabel(app, text='Choose your operating system ')
choose_os_label.place(x=20, y=310)

os_choice_box = CTk.CTkOptionMenu(app, values=["Windows", "Mac"])
os_choice_box.set('Windows')

user_os = os_choice_box.get()

download_it_for_me_button = CTk.CTkButton(
    app, text='Download it for me', command=download_it_for_me)
download_it_for_me_button.place(x=370, y=310)
os_choice_box.place(x=200, y=310)
exit_button = CTk.CTkButton(app, text="Exit", command=exit)
exit_button.place(x=430, y=501)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=270, y=501)

app.mainloop()
