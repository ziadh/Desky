import speech_recognition as sr
import tkinter as tk
import customtkinter as CTk
import subprocess
import json


def start_transcribing():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_text = r.listen(source)
    try:
        transcribed_text = r.recognize_google(audio_text)
        transcribed_text_field.configure(state='normal')
        transcribed_text_field.delete('1.0', tk.END)
        transcribed_text_field.insert(tk.END, transcribed_text)
        transcribed_text_field.configure(state='disabled')
    except sr.UnknownValueError:
        transcribed_text_field.configure(state='normal')
        transcribed_text_field.delete('1.0', tk.END)
        transcribed_text_field.insert(
            tk.END, 'Could not understand audio. Please Try again.')
        transcribed_text_field.configure(state='disabled')
    except sr.RequestError as e:
        transcribed_text_field.configure(state='normal')
        transcribed_text_field.delete('1.0', tk.END)
        transcribed_text_field.insert(
            tk.END, 'Not able to request data. Please Try again.')
        transcribed_text_field.configure(state='disabled')


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
CTk.set_default_color_theme('blue')
if theme == 'Dark':
    CTk.set_appearance_mode('Dark')
else:
    CTk.set_appearance_mode('Light')

app = CTk.CTk()
app.title(f"Voice-To-Text Transcriber v{version}")
app.geometry('400x400')
app.resizable(False, False)
welcome_label = CTk.CTkLabel(
    app, text='Welcome to Voice To Text Transcriber!', font=('Arial', 16))
welcome_label.place(x=10, y=20)
press_label = CTk.CTkLabel(
    app, text='Press the button to start transcribing....', font=('Arial', 16))
press_label.place(x=10, y=60)
transcribe_button = CTk.CTkButton(
    app, text='Start', command=start_transcribing, font=("Arial", 14))
transcribe_button.place(x=140, y=110)

ready_label = CTk.CTkLabel(app, text='Ready', font=('Arial', 16))
ready_label.place(x=180, y=140)

transcribed_text_field = tk.Text(
    app, height=10, width=47, state='disabled', wrap='word')
transcribed_text_field.insert(tk.END, 'Your speech goes here...')
transcribed_text_field.place(x=10, y=170)


exit_button = CTk.CTkButton(app, text="Exit", command=exit, font=("Arial", 14))
exit_button.place(x=240, y=350)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", command=back_to_desky)
back_to_desky_button.place(x=10, y=350)
toggle_theme_button = CTk.CTkButton(app, text="\u2600", font=(
    "Arial", 18), width=3, command=toggle_theme)
toggle_theme_button.place(x=180, y=350)
app.mainloop()
