from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Denominator Calculator")
window.geometry("600x600")
window.configure(bg="light blue")

upload = Image.open("/Images/app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(window, bg="light blue", image=image)
label.place(x=150, y=50)

label1 = Label(window, text="Welcome To The Denominator Calculator", font=("Arial", 16), bg="light blue")
label1.place(relx=0.5, y=350, anchor=CENTER)

def msg():
    msgbox = messagebox.showinfo("Alert","Do you want to start the calculations ?")
    if msgbox == "ok":
        topwin()
    

button1 = Button(window,command=msg,fg="brown",font=("Arial",16))
button1.place(x=260,y=360)

def topwin():
    top = Toplevel()
    top.configure(bg="light blue")
    top.title("Denominator Calculator")
    top.geometry("600x400")

    label = Label(top,text="Enter the total amount",bg="light grey")
    entry = Entry(top)
    lbl = Label(top,text="Here are the notes",bg="light grey")
window.mainloop()