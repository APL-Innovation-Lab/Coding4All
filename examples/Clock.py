# Import all the functions from tkinter library
from tkinter import *

# Specifically import ttk from tkinter library
from tkinter import ttk

# Import datetime class from datetime module
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the current date and time
current_time = now.strftime("%I:%M:%S")

# Print the current date and time
print("Current Time =", current_time)

# Instantiate the "Tk" class
# This means we want to use tkinter to make a window
root = Tk()
width=1000
height=500

# Make a "frame"
canvas = Canvas(root, width=width, height=height)
label = canvas.create_text( width/2, height/2, text=current_time, font=("Arial", 150))

# Create a function to update the time
def update_time():
    # get the current time
    now = datetime.now()

    # format the current time
    current_time = now.strftime("%I:%M:%S")

    # update the label with the current time
    canvas.itemconfig(label,text=current_time)
    canvas.pack(anchor=CENTER)

    # run itself again after 1000 ms
    root.after(1000, update_time)

# run the function update_time for the first time
update_time()

# Run the window
root.mainloop()