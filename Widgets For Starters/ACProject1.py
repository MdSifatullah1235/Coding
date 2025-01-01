from tkinter import *

window = Tk()
window.title("Product Calculator")
window.geometry("400x300")

lb1 = Label(text="Product Calculator", fg="#1B5E20", bg="#FFF9C4", font=("Comic Sans MS", 32), height=2, width=300)
lb1.pack()

num1_lb = Label(text="1st Number", bg="#E0F7FA", fg="#212121", font=("Comic Sans MS", 16))
num1_lb.pack()

num1_entry = Entry()
num1_entry.pack()

num2_lb = Label(text="2nd Number", bg="#E0F7FA", fg="#212121", font=("Comic Sans MS", 16))
num2_lb.pack()

num2_entry = Entry()
num2_entry.pack()

result_text = Text(height=3, width=25)
result_text.pack()

def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    product = num1 * num2
    result_text.delete(1.0, END)
    result_text.insert(1.0, str(product))

cal_btn = Button(text="Calculate", bg="#FFEB3B", fg="#0D47A1", height=1, command=calculate)
cal_btn.pack()

window.mainloop()