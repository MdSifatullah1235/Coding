from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("200x200")
window.title("Event Handler")
window.resizable(False,False)

def msg(event):
    messagebox.showwarning("Warning","Virus Detected")

button = Button(text="Click Me")
button.pack()
button.place(x=40,y=40)
button.bind("<Button-1>",msg)

window.mainloop()