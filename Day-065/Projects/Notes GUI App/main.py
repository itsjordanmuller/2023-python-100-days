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

scrollbar = ttk.Scrollbar(notes_frame, orient="vertical")
scrollbar.grid(column=1, row=1, pady=5, sticky="nsw")

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

btn_save = ttk.Button(buttons_frame, text="Save Note")
btn_save.grid(column=0, row=0, padx=5)

btn_update = ttk.Button(buttons_frame, text="Update Note")
btn_update.grid(column=1, row=0, padx=5)

btn_delete = ttk.Button(buttons_frame, text="Delete Note")
btn_delete.grid(column=2, row=0, padx=5)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)

window.mainloop()
