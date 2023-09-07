import tkinter

window = tkinter.Tk()
window.title("Python GUI Program")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I am a label!")
my_label.pack()


window.mainloop()
