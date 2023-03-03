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

class NotesApp:
    def __init__(self, master):
        self.master = master
        master.title("My Notes")
        master.geometry("1050x800")
        master.resizable(False, False)

        self.notes = []

        self.notes_list = tk.Listbox(self.master, width=50, height=41)
        self.notes_list.place(x=40, y=70)

        self.notes_list.bind("<<ListboxSelect>>", self.show_note)

        self.title_label = CTk.CTkLabel(
            self.master, text="Title:", font=('Courier New', 25))
        self.title_label.place(x=380, y=70)

        self.title_entry = CTk.CTkEntry(self.master, width=520)
        self.title_entry.place(x=480, y=70)

        self.note_text = CTk.CTkTextbox(self.master, width=620, height=620)
        self.note_text.place(x=380, y=120)

        self.save_button = CTk.CTkButton(
            self.master, text="Save", command=self.save_note, font=("Courier New", 20))
        self.save_button.place(x=520, y=750)

        self.add_button = CTk.CTkButton(
            self.master, text="Add Note", command=self.add_note)
        self.add_button.place(x=50, y=750)

        self.delete_button = CTk.CTkButton(
            self.master, text="Delete Note", command=self.delete_note)
        self.delete_button.place(x=200, y=750)

        self.load_notes()

    def load_notes(self):
        if os.path.exists("src/MN/notes.json") and os.path.getsize("src/MN/notes.json") > 0:
            with open("src/MN/notes.json", "r") as f:
                self.notes = json.load(f)
            for note in self.notes:
                self.notes_list.insert(CTk.END, note["title"])

    def save_note(self):
        title = self.title_entry.get()
        content = self.note_text.get("1.0", CTk.END)

        note = {"title": title, "content": content}

        for i in range(len(self.notes)):
            if self.notes[i]["title"] == title:
                self.notes[i] = note
                break
        else:
            self.notes.append(note)
            self.notes_list.insert(CTk.END, title)

        with open(f"src/MN/{title}.json", "w") as f:
            json.dump(note, f)

        with open("src/MN/notes.json", "w") as f:
            json.dump(self.notes, f)

        self.title_entry.delete(0, CTk.END)
        self.note_text.delete("1.0", CTk.END)

    def show_note(self, event):
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                title = self.notes_list.get(index)
                for note in self.notes:
                    if note["title"] == title:
                        self.title_entry.delete(0, CTk.END)
                        self.title_entry.insert(0, note["title"])
                        self.note_text.delete("1.0", CTk.END)
                        self.note_text.insert("1.0", note["content"])
                        break

    def add_note(self):
            self.title_entry.delete(0, CTk.END)
            self.note_text.delete("1.0", CTk.END)

    def delete_note(self):
        selection = self.notes_list.curselection()
        if selection:
            index = selection[0]
            title = self.notes_list.get(index)
            for note in self.notes:
                if note["title"] == title:
                    self.notes.remove(note)
                    self.notes_list.delete(index)
                    break

            with open("src/MN/notes.json", "w") as f:
                json.dump(self.notes, f)

            # note_file_path = f"src/MN/{title}.json"
            # if os.path.exists(note_file_path):
            #     os.remove(note_file_path)
            # else:
            #     print(f"Note file {note_file_path} not found.")



root = CTk.CTk()
app = NotesApp(root)
notes_top_title = CTk.CTkLabel(root, text='Notes', font=('Courier New', 35))
notes_top_title.place(x=10, y=20)

back_to_desky_button = CTk.CTkButton(
    root, text="Back To Desky", font=("Courier New", 20), command=back_to_desky)
back_to_desky_button.place(x=670, y=750)

exit_button = CTk.CTkButton(
    root, text="Exit", font=("Courier New", 20), command=exit)
exit_button.place(x=860, y=750)
root.mainloop()
