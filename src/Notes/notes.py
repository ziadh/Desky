import tkinter as tk
import os
import json
import customtkinter as CTk


class NotesApp:
    def __init__(self, master):
        self.master = master
        master.title("Notes App")
        master.geometry("1200x900")
        master.resizable(False, False)

        self.notes = []

        self.left_frame = CTk.CTkFrame(master, width=400, height=400)
        self.left_frame.place(x=40, y=70)

        self.notes_list = tk.Listbox(self.left_frame, width=50, height=20)
        self.notes_list.pack(fill="both", expand=True)

        self.notes_list.bind("<<ListboxSelect>>", self.show_note)

        self.title_label = CTk.CTkLabel(
            self.master, text="Title:", font=('Courier New', 25))
        self.title_label.place(x=380, y=70)

        self.title_entry = CTk.CTkEntry(self.master, width=520)
        self.title_entry.place(x=480, y=70)

        self.note_text = CTk.CTkTextbox(self.master, width=620, height=620)
        self.note_text.place(x=380, y=120)

        self.save_button = CTk.CTkButton(
            self.master, text="Save", command=self.save_note)
        self.save_button.place(x=380, y=750)

        self.add_button = CTk.CTkButton(
            self.master, text="Add Note", command=self.add_note)
        self.add_button.place(x=50, y=420)

        self.delete_button = CTk.CTkButton(
            self.master, text="Delete Note", command=self.delete_note)
        self.delete_button.place(x=200, y=420)

        self.load_notes()

    def load_notes(self):
        if os.path.exists("Notes/notes.json"):
            with open("Notes/notes.json", "r") as f:
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

        with open("Notes/notes.json", "w") as f:
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
                    os.remove(f"{title}.json")
                    break

            with open("Notes/notes.json", "w") as f:
                json.dump(self.notes, f)


root = CTk.CTk()
app = NotesApp(root)
notes_top_title = CTk.CTkLabel(root, text='Notes', font=('Courier New', 35))
notes_top_title.place(x=10, y=20)
root.mainloop()
