import webbrowser
import pyautogui as pe
from time import sleep
import customtkinter as CTk
import json
import subprocess
from tkinter import messagebox


def search():
    query = query_entry.get()
    url = f"https://chat.openai.com/chat"
    webbrowser.open(url)
    sleep(4)
    pe.typewrite(query)
    sleep(1)
    pe.press('enter')


def help():
    help_message = '''
    What does GPT Search Do?
    After you press the GPT Search button it launches your default browser and types in the query you enter here.\n\n
    Will this work if I'm not signed in to ChatGPT/OpenAI?
    No, this requires that you're signed in.\n\n
    Does this keep track of my queries?
    Not at all. This simply launches the browser and types it in for you. The source code is available at 
    https://github.ziad/ziadh/Desky if you would like to make sure for yourself. You can also run it through ChatGPT 
    itself and ask it if saves your information\n\n
    THIS PROJECT IS NOT AFFILIATED WITH CHATGPT OR OPENAI
    '''
    show_help = messagebox.showinfo('GPT Search Help', message=help_message)


def clear():
    confirm_clear = messagebox.askokcancel(
        'Confirm Clear', 'Are you sure you would like to clear the entry field?')
    if confirm_clear:
        query_entry.delete(0, 'end')


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)
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


with open('src/settings.json', 'r') as f:
    settings = json.load(f)

version = settings['version']
theme = settings['theme']

if theme == 'Dark':
    CTk.set_appearance_mode("Dark")
else:
    CTk.set_appearance_mode("Light")

app = CTk.CTk()
app.geometry('380x220')
app.resizable(False, False)
app.title(f'GPT Search v{version}')

top_title = CTk.CTkLabel(
    app, text='Welcome To GPT Search!', font=("Courier New", 20))
top_title.place(x=30, y=30)

query_entry = CTk.CTkEntry(app, width=300)
query_entry.place(x=30, y=90)
clear_button = CTk.CTkButton(app, text='Clear', command=clear, width=70)
clear_button.place(x=30, y=130)

toggle_theme_button = CTk.CTkButton(app, text="\u2600", font=(
    "Courier New", 18), width=3, command=toggle_theme)
toggle_theme_button.place(x=120, y=130)

app.bind("<Return>", lambda _: submit_button.invoke())
submit_button = CTk.CTkButton(app, text='Ask ChatGPT', command=search)
submit_button.place(x=190, y=130)

help_button = CTk.CTkButton(app, text='README', command=help, width=60)
help_button.place(x=185, y=170)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=30, y=170)

exit_button = CTk.CTkButton(app, text='Exit', command=exit, width=60)
exit_button.place(x=270, y=170)
app.mainloop()
