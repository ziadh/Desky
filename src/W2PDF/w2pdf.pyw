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


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


with open("src/settings.json", 'r')as f:
    settings = json.load(f)
theme = settings['theme']
version = settings['version']

app = CTk.CTk()
CTk.set_default_color_theme('blue')
if theme == 'dark':
    CTk.set_appearance_mode('dark')
else:
    CTk.set_appearance_mode('light')

app.resizable(False, False)
app.geometry("350x180")
app.wm_iconbitmap("assets/logos/w2pdf-logo.ico")

app.title(f"Word to PDF Converter v{version}")

label = CTk.CTkLabel(
    app, text="Please select a Word file \n\n\nFile Selected:")
label.place(x=0, y=0)

browse_button = CTk.CTkButton(app, text="Browse", command=browse_file)
browse_button.place(x=30, y=40)

convert_button = CTk.CTkButton(app, text="Convert", command=convert_to_pdf)
convert_button.place(x=180, y=40)

clear_button = CTk.CTkButton(app, text="Clear", command=clear_selection)
clear_button.place(x=30, y=90)

exit_button = CTk.CTkButton(app, text="Exit", command=exit)
exit_button.place(x=180, y=90)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=105, y=130)
app.mainloop()
