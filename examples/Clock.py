# Import all the functions from tkinter library
from tkinter import *

# Specifically import ttk from tkinter library
from tkinter import ttk

# Import datetime class from datetime module
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the current date and time
current_time = now.strftime("%H:%M:%S")

# Print the current date and time
print("Current Time =", current_time)

# Instantiate the "Tk" class
# This means we want to use tkinter to make a window
root = Tk()

# Make a "frame"
frm = ttk.Frame(root, padding=10)
frm.grid()
label = ttk.Label(frm, text=current_time)
label.grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy,).grid(column=1, row=0)

# Create a function to update the time
def update_time():
    # get the current time
    now = datetime.now()

    # format the current time
    current_time = now.strftime("%H:%M:%S")

    # update the label with the current time
    label.config(text=current_time)

    # run itself again after 1000 ms
    root.after(1000, update_time)

# run the function update_time for the first time
update_time()

# Run the window
root.mainloop()