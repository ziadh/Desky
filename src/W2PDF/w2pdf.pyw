import tkinter as tk
from tkinter import filedialog
import comtypes.client
import customtkinter as CTk
import json

global word_file
word_file = ""


def browse_file():
    global word_file
    word_file = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("Word files", "*.docx"), ("all files", "*.*")))
    if word_file == "":
        label.configure(text=f"No file has been selected")
    else:
        label.configure(text=f"File Selected: \n{word_file}")


def convert_to_pdf():
    if word_file == "":
        label.configure(text="Please select a file")
    else:
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(word_file)
        pdf_file = word_file.replace('.docx', '.pdf')
        doc.SaveAs(pdf_file, FileFormat=17)
        doc.Close()
        word.Quit()
        label.configure(text='Conversion Done, check the same folder')


def clear_selection():
    global word_file
    word_file = ""
    label.configure(text="File selection cleared.")


with open("settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']

app = CTk.CTk()
CTk.set_default_color_theme('blue')
if theme == 'dark':
    CTk.set_appearance_mode('dark')
else:
    CTk.set_appearance_mode('light')

app.resizable(False, False)
app.geometry("290x180")

app.title("Word to PDF Converter")

label = CTk.CTkLabel(
    app, text="Please select a Word file \n\n\nFile Selected:")
label.place(x=0, y=0)

browse_button = CTk.CTkButton(app, text="Browse", command=browse_file)
browse_button.place(x=0, y=40)

convert_button = CTk.CTkButton(app, text="Convert", command=convert_to_pdf)
convert_button.place(x=150, y=40)

clear_button = CTk.CTkButton(app, text="Clear", command=clear_selection)
clear_button.place(x=0, y=90)

exit_button = CTk.CTkButton(app, text="Exit", command=exit)
exit_button.place(x=150, y=90)

app.mainloop()
