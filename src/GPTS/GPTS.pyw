import webbrowser
import pyautogui as pe
from time import sleep
import customtkinter as CTk
import json
import subprocess

def search():
    query = entry.get()
    url = f"https://chat.openai.com/chat"
    print('Starting up your Browser...')
    webbrowser.open(url)
    sleep(4)
    pe.typewrite(query)
    sleep(1)
    pe.press('enter')
# TODO add a heads up function


#FIXME: finish this function
def clear():
    pass


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)

with open('settings.json', 'r') as f:
    settings = json.load(f)

version = settings['version']
theme = settings['theme']

if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

app = CTk.CTk()
app.geometry('400x400')
app.resizable(False, False)
app.title(f'GPT Search v{version}')

top_title = CTk.CTkLabel(
    app, text='Welcome To GPT Search!', font=("Courier New", 20))
top_title.place(x=30, y=30)

entry = CTk.CTkEntry(app, width=300)
entry.place(x=30, y=120)
clear_button = CTk.CTkButton(app, text='Clear', command=clear, width=70)
clear_button.place(x=30, y=160)

# TODO: bind submit to enter
submit_button = CTk.CTkButton(app, text='Ask ChatGPT', command=search)
submit_button.place(x=190, y=160)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=30, y=360)

exit_button= CTk.CTkButton(app,text='Exit',command=exit,width=60)
exit_button.place(x=270,y=360)
app.mainloop()
