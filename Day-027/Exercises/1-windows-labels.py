from tkinter import *

# Create main window
window = Tk()
window.title("Python GUI Program")
window.minsize(width=500, height=400)

# Initialize a label
my_label = Label(text="I am a label!", font=("Arial", 24, "bold"))
my_label.pack()

# Update label text
my_label["text"] = "New Label Text!"
my_label.config(text="Yet Another Label!")

# Counter for button clicks
i = 0


# Function to handle button click (increments counter)
def button_clicked():
    global i
    print("Button was clicked!")
    i += 1
    my_label["text"] = f"Button Clicked {i} Times!"


# Function to update label with input field text
def input_label():
    input_value = input.get()
    my_label["text"] = input_value


# Button to trigger increment function
button = Button(text="Increment!", command=button_clicked)
button.pack()

# Button to update label with input field text
button = Button(text="Get Input!", command=input_label)
button.pack()

# Input field
input = Entry(width=10)
input.pack()

# Start the main event loop
window.mainloop()
