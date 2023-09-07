import tkinter

window = tkinter.Tk()
window.title("Python GUI Program")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I am a label!", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

my_label["text"] = "New Label Text!"
my_label.config(text="Yet Another Label!")

window.mainloop()
