import webbrowser
from tkinter import *
import customtkinter as CTk
from tkinter import messagebox
import subprocess
import json
import platform
import urllib.request

CTk.set_appearance_mode("Dark")
CTk.set_default_color_theme("blue")

# TODO: add a suggest app function soon™


def open_downloads():
    vars_list = [bnetvar.get(), spotifyvar.get(), chromevar.get(), firefoxvar.get(), discordvar.get(),
                 vscvar.get(), ghdvar.get(), npppvar.get(), skypevar.get(), steamvar.get(), evernotevar.get(), itunesvar.get(), gitvar.get()]
    if not any(var == 1 for var in vars_list):
        result = messagebox.showinfo(
            title="Nothing selected", message="Please select at least one.")
    else:
        if bnetvar.get() == 1:
            webbrowser.open(
                "https://www.blizzard.com/en-us/apps/battle.net/desktop")
        if spotifyvar.get() == 1:
            webbrowser.open("https://www.spotify.com/us/download/")
        if chromevar.get() == 1:
            webbrowser.open("https://www.google.com/chrome/")
        if firefoxvar.get() == 1:
            webbrowser.open("https://www.mozilla.org/en-US/firefox/new/")
        if discordvar.get() == 1:
            webbrowser.open("https://discord.com/download")
        if vscvar.get() == 1:
            webbrowser.open("https://code.visualstudio.com/download")
        if ghdvar.get() == 1:
            webbrowser.open("https://desktop.github.com/")
        if npppvar.get() == 1:
            webbrowser.open("https://notepad-plus-plus.org/downloads/")
        if skypevar.get() == 1:
            webbrowser.open("https://www.skype.com/en/get-skype/")
        if steamvar.get() == 1:
            webbrowser.open("https://store.steampowered.com/about/")
        if evernotevar.get() == 1:
            webbrowser.open("https://evernote.com/download")
        if itunesvar.get() == 1:
            webbrowser.open("https://support.apple.com/downloads/itunes")
        if gitvar.get() == 1:
            webbrowser.open("https://git-scm.com/downloads")
        reset_selections()


def reset_selections():
    bnetvar.set(0)
    spotifyvar.set(0)
    chromevar.set(0)
    firefoxvar.set(0)
    discordvar.set(0)
    vscvar.set(0)
    ghdvar.set(0)
    npppvar.set(0)
    skypevar.set(0)
    steamvar.set(0)
    evernotevar.set(0)
    itunesvar.set(0)
    gitvar.set(0)


def select_all():
    bnetvar.set(1)
    spotifyvar.set(1)
    chromevar.set(1)
    firefoxvar.set(1)
    discordvar.set(1)
    vscvar.set(1)
    ghdvar.set(1)
    npppvar.set(1)
    skypevar.set(1)
    steamvar.set(1)
    evernotevar.set(1)
    itunesvar.set(1)
    gitvar.set(1)


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def download_it_for_me():
    with open('src/apps.json', 'r') as f:
        apps = json.load(f)
    vars_list = {'BattleNet': bnetvar.get(),
                 'Spotify': spotifyvar.get(),
                 'Chrome': chromevar.get(),
                 'Firefox': firefoxvar.get(),
                 'Discord': discordvar.get(),
                 'VSC': vscvar.get(),
                 'GitHubDesktop': ghdvar.get(),
                 'Notepad++': npppvar.get(),
                 'Skype': skypevar.get(),
                 'Steam': steamvar.get(),
                 'Evernote': evernotevar.get(),
                 'iTunes': itunesvar.get(),
                 'Git': gitvar.get()}
    selected_apps = [app_name for app_name,
                     var in vars_list.items() if var == 1]
    if not selected_apps:
        result = messagebox.showinfo(
            title="Nothing selected", message="Please select at least one.")
    else:
        for app_name in selected_apps:
            app_data = next(
                (app for app in apps['applications'] if app['name'] == app_name), None)
            if app_data:
                download_link = app_data[f'{user_platform}_download_link']
                webbrowser.open(download_link)
                reset_selections()

def toggle_theme():
    with open("src/settings.json", "r")as f:
        settings = json.load(f)
    theme = settings['theme']
    if theme == 'Dark':
        CTk.set_appearance_mode("Light")
        toggle_theme_button.configure(text="\u26ee")
        settings['theme'] = 'Light'
    if theme == 'Light':
        CTk.set_appearance_mode("Dark")
        toggle_theme_button.configure(text="\u2600")
        settings['theme'] = 'Dark'
    with open('src/settings.json', 'w') as f:
        json.dump(settings, f)

with open("src/settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']
version = settings['version']


app = CTk.CTk()
app.title(f"Fresh Desktop Checklist v{version}")
app.wm_iconbitmap("assets/logos/FDCL-logo.ico")

app.geometry("600x450")
app.resizable(False, False)
bnetvar = IntVar()
spotifyvar = IntVar()
chromevar = IntVar()
firefoxvar = IntVar()
discordvar = IntVar()
vscvar = IntVar()
ghdvar = IntVar()
npppvar = IntVar()
skypevar = IntVar()
steamvar = IntVar()
evernotevar = IntVar()
itunesvar = IntVar()
gitvar = IntVar()


if theme == 'Dark':
    CTk.set_appearance_mode("Dark")
else:
    CTk.set_appearance_mode("Light")

BattleNet = CTk.CTkCheckBox(app, text="BattleNet", variable=bnetvar)
Chrome = CTk.CTkCheckBox(app, text="Chrome", variable=chromevar)
evernote = CTk.CTkCheckBox(app, text="Evernote", variable=evernotevar)
discord = CTk.CTkCheckBox(app, text="Discord", variable=discordvar)
firefox = CTk.CTkCheckBox(app, text="Firefox", variable=firefoxvar)
itunes = CTk.CTkCheckBox(app, text="iTunes", variable=itunesvar)
git = CTk.CTkCheckBox(app, text="Git", variable=gitvar)
ghd = CTk.CTkCheckBox(app, text="GitHub Desktop", variable=ghdvar)
np = CTk.CTkCheckBox(app, text="NotePad++", variable=npppvar)
skype = CTk.CTkCheckBox(app, text="Skype", variable=skypevar)
spotify = CTk.CTkCheckBox(app, text="Spotify", variable=spotifyvar)
steam = CTk.CTkCheckBox(app, text="Steam", variable=steamvar)
vs = CTk.CTkCheckBox(app, text="VS Code", variable=vscvar)

BattleNet.place(x=10, y=90)
Chrome.place(x=10, y=120)
evernote.place(x=10, y=150)
discord.place(x=140, y=90)
firefox.place(x=140, y=120)
git.place(x=140, y=150)
ghd.place(x=270, y=90)
itunes.place(x=270, y=120)
np.place(x=270, y=150)
skype.place(x=400, y=90)
spotify.place(x=400, y=120)
steam.place(x=400, y=150)
vs.place(x=480, y=90)
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

download_it_for_me_label = CTk.CTkLabel(
    app, text='Download them for me: ', font=("Arial", 15))
download_it_for_me_label.place(x=20, y=280)

choose_os_label = CTk.CTkLabel(
    app, text='Choose your operating system ', font=("Arial", 12))
choose_os_label.place(x=20, y=310)

os_choice_box = CTk.CTkOptionMenu(app, values=["Windows", "Mac"])
os_choice_box.set('Windows')

user_os = os_choice_box.get()
user_platform = user_os.lower()
download_it_for_me_button = CTk.CTkButton(
    app, text='One-Click Download', command=download_it_for_me)
download_it_for_me_button.place(x=350, y=310)
os_choice_box.place(x=200, y=310)
exit_button = CTk.CTkButton(app, text="Exit", command=exit)
exit_button.place(x=430, y=401)

toggle_theme_button = CTk.CTkButton(app, text="\u2600", font=(
    "Arial", 18), width=3, command=toggle_theme)
toggle_theme_button.place(x=220, y=401)
back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=270, y=401)

app.mainloop()
