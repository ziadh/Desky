import webbrowser
import pyautogui as pe
from time import sleep
import customtkinter as CTk
import json
def search():
    query = entry.get()
    url = f"https://chat.openai.com/chat"
    print('Starting up your Browser...')
    webbrowser.open(url)
    sleep(4)
    pe.typewrite(query)
    sleep(1)
    pe.press('enter')
#TODO add a theme function
#TODO add a back to desky button
#TODO add a heads up function
#TODO add an exit button
#TODO add a top label 

with open('settings.json','r') as f:
    settings=json.load(f)

version=settings['version']
theme=settings['theme']

app = CTk.CTk()
app.geometry('400x400')
app.resizable(False,False)
app.title(f'GPT Search v{version}')
entry = CTk.CTkEntry(app)
entry.pack()
submit_button = CTk.CTkButton(app,text='Ask ChatGPT',command=search)
submit_button.pack()

app.mainloop()