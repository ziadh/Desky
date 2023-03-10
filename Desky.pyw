import customtkinter as CTk
import json
from tkinter import *
import subprocess
import requests
import webbrowser
from tkinter import messagebox
import sys
import os
import time

file_path = None
language = None

log_folder = "errors_logged"
log_prefix = "errors_log_from_.txt"

if not os.path.exists(log_folder):
    os.makedirs(log_folder)
current_time = time.strftime("%m%d%Y-%H-%M-%S")
log_file = log_prefix + current_time + ".txt"
log_path = os.path.join(log_folder, log_file)
sys.stderr = open(log_path, "a")


def update_username():
    global change_username_entry
    change_username_entry = CTk.CTkEntry(app, width=230)
    change_username_entry.focus()
    change_username_entry.place(x=10, y=50)
    global update_password_button
    update_password_button = CTk.CTkButton(
        app, text="\u2714", width=5, font=("Courier New", 20), command=save_username)
    update_password_button.place(x=250, y=50)
    global cancel_change_button
    cancel_change_button = CTk.CTkButton(app, width=5, text="\u274C", font=("Courier New", 20), command=cancel_username_changes)
    cancel_change_button.place(x=290, y=50)


def save_username():
    global username
    username = change_username_entry.get()

    with open("user_settings.json", "r+") as json_file:
        data = json.load(json_file)
        data["username"] = username
        if not username:
            username = "New User"
            data["username"] = username

    welcome_label.configure(text=f"Welcome, {username}!")
    cancel_username_changes()

    with open('user_settings.json', 'w') as f:
        json.dump(data, f)


def cancel_username_changes():
    update_password_button.destroy()
    change_username_entry.destroy()
    cancel_change_button.destroy()


def open_YTD():
    app.destroy()
    subprocess.run(["python", "src/YTD/YTD.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def open_DSP():
    app.destroy()
    subprocess.run(["python", "src/DSP/DSP.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def open_DO():
    app.destroy()
    subprocess.run(["python", "src/DO/do.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def open_W2PDF():
    app.destroy()
    subprocess.run(["python", "src/W2PDF/w2pdf.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def open_V2TXT():
    app.destroy()
    subprocess.run(["python", "src/V2TXT/V2TXT.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def open_FDCL():
    app.destroy()
    subprocess.run(["python", "src/FD/FDCL.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def open_TT():
    app.destroy()
    subprocess.run(["python", "src/TT/TT.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def open_PCW():
    app.destroy()
    subprocess.run(["python", "src/PCW/PCW.pyw"],
                       creationflags=subprocess.CREATE_NO_WINDOW)

def open_QRG():
    app.destroy()
    subprocess.run(["python", "src/QRG/QRG.pyw"],
                       creationflags=subprocess.CREATE_NO_WINDOW)
def open_MN():
    app.destroy()
    subprocess.run(["python", "src/MN/MN.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def toggle_theme():
    with open("settings.json", "r")as f:
        settings = json.load(f)
    theme = settings['theme']
    if theme == 'dark':
        CTk.set_appearance_mode("light")
        toggle_theme_button.configure(text="\u26ee")
        settings['theme'] = 'light'
    if theme == 'light':
        CTk.set_appearance_mode("dark")
        toggle_theme_button.configure(text="\u2600")
        settings['theme'] = 'dark'
    with open('settings.json', 'w') as f:
        json.dump(settings, f)



def check_for_updates():
    r = requests.get("https://api.github.com/repos/ziadh/Desky/releases")
    json_data = r.json()
    newest_version = json_data[0]["tag_name"]
    if float(newest_version) > float(version):
        version_message.configure(text=f"New update v{newest_version} available. Click me to update.")
        version_message.bind("<Button-1>", download_update)
    else:
        whats_new_label.configure(text=f"You are running the latest version v{version}. Click me to view\nthe latest changes.")
        whats_new_label.bind("<Button-1>", open_release_notes)



def open_release_notes(event):
    r = requests.get("https://api.github.com/repos/ziadh/Safe-Data/releases")
    json_data = r.json()
    newest_version = json_data[0]["tag_name"]
    notes_link = f"https://github.com/ziadh/Safe-Data/releases/tag/{newest_version}"
    webbrowser.open(notes_link)


def download_update(event):
    r = requests.get("https://api.github.com/repos/ziadh/Desky/releases")
    json_data = r.json()
    newest_version = json_data[0]["tag_name"]
    link = "https://github.com/ziadh/Desky/archive/refs/tags/"+newest_version+".zip"
    webbrowser.open(link)


def exit_app():
    confirm = messagebox.askyesno(
        title='Confirm Exit', message=' Are you sure you would like to exit?')
    if confirm:
        app.destroy()


def open_github_page():
    link = "https://github.com/ziadh/Desky/"
    webbrowser.open(link)


with open("settings.json", 'r')as f:
    settings = json.load(f)
with open("user_settings.json", 'r')as f:
    user_settings = json.load(f)
version = settings['version']
username = user_settings['username']
theme = settings['theme']

if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

CTk.set_default_color_theme("blue")


app = CTk.CTk()
app.bind("<Return>", lambda _: update_password_button.invoke())
app.bind("<Escape>", lambda _: cancel_change_button.invoke())
app.geometry("600x630")
app.title(f"Desky v{version}")
app.resizable(False, False)
app.wm_iconbitmap('assets/logos/Desky-logo.ico')

welcome_label = CTk.CTkLabel(
    app, text=f"Welcome, {username}!", font=("Courier New", 22))


welcome_label.place(x=10, y=10)
change_username_button = CTk.CTkButton(
    app, text="Change Name", font=("Courier New", 22), command=update_username)
change_username_button.place(x=430, y=10)

top_seperator = CTk.CTkLabel(
    app, text="^"*157)
top_seperator.place(x=-20, y=50)

apps_label = CTk.CTkLabel(app, text="My Apps", font=("Courier New", 22))
apps_label.place(x=250, y=70)

DSP_button = CTk.CTkButton(app, text="Daily Sneak Peek", font=(
    "Courier New", 22), command=open_DSP)
DSP_button.place(x=10, y=110)
DO_button = CTk.CTkButton(app, text="Downloads Organizer", font=(
    "Courier New", 22), command=open_DO)
DO_button.place(x=10, y=170)

FDCL_button = CTk.CTkButton(app, text="Fresh Desktop Checklist",
                            font=("Courier New", 22), command=open_FDCL)
FDCL_button.place(x=10, y=230)

MN_button = CTk.CTkButton(app, text="My Notes",
                            font=("Courier New", 22), command=open_MN, anchor="w",width=20)
MN_button.place(x=10, y=290)
PCW_button = CTk.CTkButton(app, text="PC Watcher", font=("Courier New", 22), command=open_PCW, width=20, anchor="w")
PCW_button.place(x=10, y=350)

QRG_button = CTk.CTkButton(app, text="QR Generator", font=("Courier New", 22), command=open_QRG, width=20, anchor="w")
QRG_button.place(x=10, y=410)

TT_button = CTk.CTkButton(app, text='Tock Tick',
                          font=("Courier New", 22), command=open_TT, width=20, anchor="w")
TT_button.place(x=10, y=470)


W2PDF_button = CTk.CTkButton(app, text="Word To PDF", font=(
    "Courier New", 22), command=open_W2PDF)
W2PDF_button.place(x=410, y=110)

v2txt_button = CTk.CTkButton(app, text="Voice to Text", font=(
    "Courier New", 22), command=open_V2TXT)
v2txt_button.place(x=410, y=170)

YTD_button = CTk.CTkButton(app, text="YT Downloader", font=(
    "Courier New", 22), command=open_YTD)
YTD_button.place(x=410, y=230)

bottom_seperator = CTk.CTkLabel(app, text="v"*157)
bottom_seperator.place(x=-20, y=510)


github_page_button = CTk.CTkButton(
    app, text='GitHub', width=30, command=open_github_page)
github_page_button.place(x=110, y=585)

toggle_theme_button = CTk.CTkButton(app, text="\u2600", font=(
    "Courier New", 18), width=3, command=toggle_theme)
toggle_theme_button.place(x=385, y=585)
check_for_updates_button = CTk.CTkButton(app, text="Check for Updates", font=(
    "Courier New", 18), command=check_for_updates)
check_for_updates_button.place(x=170, y=585)

exit_button = CTk.CTkButton(app, text="Exit", font=(
    "Courier New", 18), command=exit_app)
exit_button.place(x=430, y=585)


version_message = CTk.CTkLabel(app, text="", font=("Courier New", 16))
version_message.place(x=0, y=530)
whats_new_label = CTk.CTkLabel(app,text="", font=("Courier New", 16))
whats_new_label.place(x=0, y=530)

app.mainloop()

sys.stderr.close()
if os.path.getsize(log_path) == 0:
    os.remove(log_path)
    os.rmdir(log_folder)
