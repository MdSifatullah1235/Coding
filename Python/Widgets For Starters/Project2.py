from tkinter import *
from datetime import date
window = Tk()
window.title("Demo App")
window.geometry("400x200")

lb1 = Label(text="Hi There", fg="blue", bg="#55f244", font=("Arial",16), height=2, width=200)
name_lb = Label(text="Full Name", bg="#55f244")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message 
    message = " Welcome to my app \n Todays Date is: "
    greet =  "Hello", name
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert (END, date.today())

text_box = Text(height=3)

btn = Button(text="Lets Start", command=display, height=1,bg="#55f244",fg="white")
lb1.pack()
name_lb.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()