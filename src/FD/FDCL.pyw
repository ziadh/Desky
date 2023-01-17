import webbrowser
from tkinter import *
import customtkinter
from tkinter import messagebox

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


def open_downloads():
    vars_list = [var1.get(), var2.get(), var3.get(), var4.get(),
                 var5.get(), var6.get(), var7.get(), var8.get()]
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


def select_all():
    var1.set(1)
    var2.set(1)
    var3.set(1)
    var4.set(1)
    var5.set(1)
    var6.set(1)
    var7.set(1)
    var8.set(1)


app = customtkinter.CTk()
app.title("Fresh Desktop Checklist")
app.geometry("450x380")
app.resizable(False, False)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

chrome = customtkinter.CTkCheckBox(app, text="Chrome", variable=var2)
discord = customtkinter.CTkCheckBox(app, text="Discord", variable=var4)
firefox = customtkinter.CTkCheckBox(app, text="Firefox", variable=var3)
ghd = customtkinter.CTkCheckBox(app, text="GitHub Desktop", variable=var6)
np = customtkinter.CTkCheckBox(app, text="NotePad++", variable=var7)
skype = customtkinter.CTkCheckBox(app, text="Skype", variable=var8)
spotify = customtkinter.CTkCheckBox(app, text="Spotify", variable=var1)
vs = customtkinter.CTkCheckBox(app, text="VS Code", variable=var5)

chrome.place(x=120, y=110)
discord.place(x=120, y=140)
firefox.place(x=120, y=170)
ghd.place(x=120, y=200)
np.place(x=270, y=110)
skype.place(x=270, y=140)
spotify.place(x=270, y=170)
vs.place(x=270, y=200)
msg = """
Welcome to Fresh Desktop Downloads. If your computer recently got through\na factory reset, simply check the boxes for the applications that you would like\nto install then press the download button.
"""
welcome_label = customtkinter.CTkLabel(
    app, text=msg, justify=LEFT, padx=10, pady=10)
welcome_label.grid(row=0, column=0)
download_button = customtkinter.CTkButton(
    app, text="Download", command=open_downloads)
download_button.place(x=70, y=310)
exit_button = customtkinter.CTkButton(
    app, text="Exit", command=exit)
exit_button.place(x=250, y=310)

select_all_button = customtkinter.CTkButton(
    app, text="Select All", command=select_all)
select_all_button.place(x=70, y=272)

clear_selection_button = customtkinter.CTkButton(
    app, text="Clear Selection", command=reset_selections)
clear_selection_button.place(x=250, y=272)


app.mainloop()
