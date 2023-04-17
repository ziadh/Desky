import tkinter as tk
from tkinter import filedialog
import comtypes.client
import customtkinter as CTk
import json
import subprocess

global word_file
word_file = ""


def browse_file():
    global word_file
    word_file = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("Word files", "*.docx"), ("all files", "*.*")))
    if word_file == "":
        select_label.configure(text=f"No file has been selected")
    else:
        select_label.configure(text=f"File Selected: \n{word_file}")


def convert_to_pdf():
    if word_file == "":
        select_label.configure(text="Please select a file")
    else:
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(word_file)
        pdf_file = word_file.replace('.docx', '.pdf')
        doc.SaveAs(pdf_file, FileFormat=17)
        doc.Close()
        word.Quit()
        select_label.configure(text='Conversion Done, check the same folder')


def clear_selection():
    global word_file
    word_file = ""
    select_label.configure(text="File selection cleared.")


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


with open("src/settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']
version = settings['version']

app = CTk.CTk()
CTk.set_default_color_theme('blue')
if theme == 'Dark':
    CTk.set_appearance_mode('Dark')
else:
    CTk.set_appearance_mode('Light')

app.resizable(False, False)
app.geometry("350x320")
app.wm_iconbitmap("assets/logos/w2pdf-logo.ico")

app.title(f"Word to PDF Converter v{version}")

top_label = CTk.CTkLabel(app, text="Welcome to Word to PDF Converter!", font=("Arial", 17))
top_label.place(x=20, y=30)
select_label = CTk.CTkLabel(
    app, text="Please select a Word file \n\n\nFile Selected: None", font=(
        "Arial", 14))
select_label.place(x=20, y=90)

browse_button = CTk.CTkButton(
    app, text="Browse", command=browse_file, font=("Arial", 14))
browse_button.place(x=30, y=180)

convert_button = CTk.CTkButton(app, text="Convert", command=convert_to_pdf, font=("Arial", 14))
convert_button.place(x=180, y=180)

clear_button = CTk.CTkButton(app, text="Clear", command=clear_selection, font=("Arial", 14))
clear_button.place(x=30, y=230)

exit_button = CTk.CTkButton(app, text="Exit", command=exit, font=("Arial", 14))
exit_button.place(x=180, y=230)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky, font=("Arial", 14))
back_to_desky_button.place(x=105, y=270)

toggle_theme_button = CTk.CTkButton(app, text="\u2600", font=(
    "Arial", 18), width=3, command=toggle_theme)
toggle_theme_button.place(x=290, y=270)
app.mainloop()
