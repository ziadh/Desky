import customtkinter as CTk
import psutil
import platform
import subprocess
import json

app = CTk.CTk()
app.geometry('400x400')
app.resizable(False, False)


with open("src/settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']
version = settings['version']
app.title(f'PC Watcher v{version}')


CTk.set_default_color_theme("blue")
if theme == 'Dark':
    CTk.set_appearance_mode("Dark")
else:
    CTk.set_appearance_mode("Light")


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def show_sysinfo():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    platform_info = platform.system() + ' ' + platform.release()
    sysinfo = f"""
    CPU Usage: {cpu_percent}% \n
    Memory Usage: {memory_info.percent}% \n
    Disk Usage: {disk_info.percent}% \n
    Platform: {platform_info}\n 
    """
    sysinfo_label.configure(text=sysinfo)
    app.after(1000, show_sysinfo)


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


top_label = CTk.CTkLabel(app, text="PC Watcher", font=('Arial', 25))
top_label.place(x=140, y=50)
sysinfo_label = CTk.CTkLabel(app, text="", font=('Arial', 18), justify="left")
sysinfo_label.place(x=20, y=100)
back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=40, y=355)
toggle_theme_button = CTk.CTkButton(app, text="\u2600", font=(
    "Arial", 18), width=3, command=toggle_theme)
toggle_theme_button.place(x=190, y=355)
exit_button = CTk.CTkButton(app, text='Exit', command=exit)
exit_button.place(x=230, y=355)

show_sysinfo()
app.mainloop()
