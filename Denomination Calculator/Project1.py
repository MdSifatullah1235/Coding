from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


window = Tk()
window.title("Denominator Calculator")
window.geometry("600x600")
window.configure("light blue")

upload = Image.open("./Images/app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(window,bg="light blue",image=image)
label.place(x=150,y=50)

label1 = Label(window,text="Welcome To The Denominator Calculator",font=("Arial",16),bg="light blue")

label1.place(relx=0.5,y=350,anchor=CENTER)
