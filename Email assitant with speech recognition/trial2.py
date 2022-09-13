from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

def display_msg():
   messagebox.showinfo("Message", "Hello There! Greeting from TutorialsPoint.")
def hide_button(widget):
   widget.pack_forget()

# Add a Button widget
b1 = ttk.Button(win, text="Click Me", command=display_msg)
b1.pack(pady=30)
b2 = ttk.Button(win, text="Click Me", command=lambda: hide_button(b1))
b2.pack(pady=60)
b1.invoke()

win.mainloop()