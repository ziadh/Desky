import tkinter as tk
import os
import json
import customtkinter as CTk
import subprocess


with open("settings.json", 'r')as f:
    settings = json.load(f)

version = settings['version']
theme = settings['theme']

if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def load_notes():
    if os.path.exists("src/MN/notes.json") and os.path.getsize("src/MN/notes.json") > 0:
        with open("src/MN/notes.json", "r") as f:
            notes = json.load(f)
        for note in notes:
            notes_list.insert(CTk.END, note["title"])


def save_notes(notes):
    with open("src/MN/notes.json", "w") as f:
        json.dump(notes, f)


def save_note():
    title = title_entry.get()
    content = note_text.get("1.0", CTk.END)

    note = {"title": title, "content": content}

    for i in range(len(notes)):
        if notes[i]["title"] == title:
            notes[i] = note
            break
    else:
        notes.append(note)
        notes_list.insert(CTk.END, title)

    save_notes(notes)

    title_entry.delete(0, CTk.END)
    note_text.delete("1.0", CTk.END)


def show_note(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        title = notes_list.get(index)
        for note in notes:
            if note["title"] == title:
                title_entry.delete(0, CTk.END)
                title_entry.insert(0, note["title"])
                note_text.delete("1.0", CTk.END)
                note_text.insert("1.0", note["content"])
                break


def add_note():
    title_entry.delete(0, CTk.END)
    note_text.delete("1.0", CTk.END)


def delete_note():
    selection = notes_list.curselection()
    if selection:
        index = selection[0]
        title = notes_list.get(index)
        for note in notes:
            if note["title"] == title:
                notes.remove(note)
                notes_list.delete(index)
                break

        save_notes(notes)
    load_notes()


app = CTk.CTk()
app.title(f"My Notes v{version}")
app.geometry("1050x800")
app.resizable(False, False)

notes = []

notes_list = tk.Listbox(app, width=50, height=41)
notes_list.place(x=40, y=70)

notes_list.bind("<<ListboxSelect>>", show_note)

title_label = CTk.CTkLabel(
    app, text="Title:", font=('Courier New', 25))
title_label.place(x=380, y=70)

title_entry = CTk.CTkEntry(app, width=520)
title_entry.place(x=480, y=70)

note_text = CTk.CTkTextbox(app, width=620, height=620)
note_text.place(x=380, y=120)

save_button = CTk.CTkButton(
    app, text="Save", command=save_note, font=("Courier New", 20))
save_button.place(x=530, y=750)

add_button = CTk.CTkButton(
    app, text="+", command=add_note, width=50)
add_button.place(x=40, y=750)

delete_button = CTk.CTkButton(
    app, text="-", command=delete_note, width=50)
delete_button.place(x=160, y=750)

refresh_button = CTk.CTkButton(
    app, text="\u27F3", command=load_notes, width=50)
refresh_button.place(x=290, y=750)


load_notes()

notes_top_title = CTk.CTkLabel(app, text='Notes', font=('Courier New', 35))
notes_top_title.place(x=10, y=20)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", font=("Courier New", 20), command=back_to_desky)
back_to_desky_button.place(x=680, y=750)

exit_button = CTk.CTkButton(
    app, text="Exit", font=("Courier New", 20), command=exit)
exit_button.place(x=860, y=750)
app.mainloop()
