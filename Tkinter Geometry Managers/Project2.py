from tkinter import *

window = Tk()
window.title("Login Page")
window.geometry('400x400')

frame = Frame(master=window, height=300, width=360, bg="#d0efff")

lbl1 = Label(master=frame, text="Username", bg="#d0efff", font=("Arial", 18))
lbl2 = Label(master=frame, text="Email", bg="#d0efff", font=("Arial", 18))
lbl3 = Label(master=frame, text="Password", bg="#d0efff", font=("Arial", 18))

name_entry = Entry(master=frame, width=50)
email_entry = Entry(master=frame, width=50)
password_entry = Entry(master=frame, width=50, show='*')

def display():
    name = name_entry.get()
    greet = "Hello", name
    message = "\nLogin successful!"
    text_box.insert(END, greet)
    text_box.insert(END, message)

text_box = Text(bg="#BEBEBE", fg="black", font=("Arial", 12), height=5, width=40)


btn = Button(text="Login", command=display, height=2, width=25, bg='#3895D3', fg='white')

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=25, y=50)
lbl2.place(x=20, y=80)
email_entry.place(x=25, y=110)
lbl3.place(x=20, y=140)
password_entry.place(x=25, y=170)
btn.place(x=100, y=200)
text_box.place(x=20, y=250)

window.mainloop()