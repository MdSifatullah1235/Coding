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

    l1 = Label(top,text="2000",bg="light grey")
    l2 = Label(top,text="500",bg="light grey")
    l3 = Label(top,text="100",bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculation():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount = amount % 2000
            note500 = amount // 500
            amount = amount % 500
            note100 = amount // 100
            amount = amount % 100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))

        except ValueError:
            messagebox.showerror("Error","Please Give A Valid Input")

    btn = Button(top,command=calculation,text="Calculate",bg="brown",fg="white")

    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=160,y=260)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    
window.mainloop()