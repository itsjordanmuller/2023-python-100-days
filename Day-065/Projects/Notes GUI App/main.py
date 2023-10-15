import tkinter as tk
from tkinter import scrolledtext, ttk

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///notes.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)


Base.metadata.create_all(engine)

selected_note_id = None


def save_note():
    title = ent_title.get().strip()
    content = txt_note.get("1.0", tk.END).strip()
    if title and content:
        new_note = Note(title=title, content=content)
        session.add(new_note)
        session.commit()
        load_notes()
        clear_fields()


def update_note():
    global selected_note_id
    if selected_note_id is not None:
        new_title = ent_title.get().strip()
        new_content = txt_note.get("1.0", tk.END).strip()
        if new_title and new_content:
            note = session.query(Note).get(selected_note_id)
            note.title = new_title
            note.content = new_content
            session.commit()
            load_notes()
            clear_fields()
            selected_note_id = None


def delete_note():
    selected_note = lst_notes.curselection()
    if selected_note:
        note_id = notes[selected_note[0]].id
        note = session.query(Note).get(note_id)
        session.delete(note)
        session.commit()
        load_notes()
        clear_fields()


def load_notes():
    global notes
    notes = session.query(Note).all()
    lst_notes.delete(0, tk.END)
    for note in notes:
        display_text = (note.title + " - " + note.content)[:48]
        if len((note.title + " - " + note.content)) > 48:
            display_text += "..."
        lst_notes.insert(tk.END, display_text)


def clear_fields():
    ent_title.delete(0, tk.END)
    txt_note.delete("1.0", tk.END)


def on_note_select(event):
    global selected_note_id
    selected_note = lst_notes.curselection()
    if selected_note:
        note = notes[selected_note[0]]
        selected_note_id = note.id
        ent_title.delete(0, tk.END)
        ent_title.insert(tk.END, note.title)
        txt_note.delete("1.0", tk.END)
        txt_note.insert(tk.END, note.content)


window = tk.Tk()
window.title("Notes App")
window.config(bg="#2f3640", padx=10, pady=10)

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12), padding=5)

notes_frame = tk.Frame(window)
notes_frame.grid(column=0, row=0, sticky="nsw")

lbl_saved_notes = ttk.Label(notes_frame, text="Saved Notes:")
lbl_saved_notes.grid(column=0, row=0, sticky="w", padx=5, pady=5)

lst_notes = tk.Listbox(notes_frame, width=38, height=15, bg="#F0F0F0")
lst_notes.grid(column=0, row=1, sticky="w", padx=5, pady=5)
lst_notes.bind("<<ListboxSelect>>", on_note_select)

scrollbar = ttk.Scrollbar(notes_frame, orient="vertical", command=lst_notes.yview)
scrollbar.grid(column=1, row=1, pady=5, sticky="nsw")
lst_notes.configure(yscrollcommand=scrollbar.set)

edit_frame = tk.Frame(window)
edit_frame.grid(column=1, row=0, sticky="nsew")

lbl_title = ttk.Label(edit_frame, text="Note Title:")
lbl_title.grid(column=0, row=0, sticky="nw", padx=5, pady=5)

ent_title = ttk.Entry(edit_frame, width=52)
ent_title.grid(column=0, row=1, padx=5, pady=5, sticky="nw")

lbl_note = ttk.Label(edit_frame, text="Note Content:")
lbl_note.grid(column=0, row=2, sticky="nw", padx=5, pady=5)

txt_note = scrolledtext.ScrolledText(edit_frame, wrap=tk.WORD, width=52, height=14)
txt_note.grid(column=0, row=3, padx=5, pady=5, sticky="nw")

buttons_frame = tk.Frame(notes_frame)
buttons_frame.grid(column=0, row=3, padx=5, pady=5, sticky="sw", columnspan=2)

btn_save = ttk.Button(buttons_frame, text="Save Note", command=save_note)
btn_save.grid(column=0, row=0, padx=5)

btn_update = ttk.Button(buttons_frame, text="Update Note", command=update_note)
btn_update.grid(column=1, row=0, padx=5)

btn_delete = ttk.Button(buttons_frame, text="Delete Note", command=delete_note)
btn_delete.grid(column=2, row=0, padx=5)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)

load_notes()

window.mainloop()
