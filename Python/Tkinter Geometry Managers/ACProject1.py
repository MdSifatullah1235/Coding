from tkinter import *
from datetime import datetime

def calculate():
    year = year_entry.get()
    current_year = datetime.now().year
    age = current_year - int(year)
    text_box.delete(1.0, END)  
    message = f"You are {age} years old.\n"
    text_box.insert(END, message)

window = Tk()
window.title("Age Calculator")
window.geometry('400x400')

year_lb = Label(text="Birth Year", font=("Arial", 16))
year_lb.place(x=100, y=100)

year_entry = Entry(width=25)
year_entry.place(x=100, y=140)

calc_btn = Button(command=calculate, text="Calculate", height=2, width=12, bg='#f01d59', fg='white')
calc_btn.place(x=125, y=180)

text_box = Text(bg="#BEBEBE", fg="black", font=("Arial", 12), height=5, width=17)
text_box.place(x=100, y=250)

window.mainloop()
