from tkinter import *

def calculate():
    p = float(principal.get())
    t = float(time.get())
    r = float(rate.get())
    si = (p * t * r) / 100
    ci = p * ((1 + r / 100) ** t) - p
    result.config(text=f"SI: {si}\nCI: {ci}")

app = Tk()
app.geometry("400x400")
app.title("Calculator")

Label(app, text="Principal").pack()
principal = Entry(app)
principal.pack()

Label(app, text="Time").pack()
time = Entry(app)
time.pack()

Label(app, text="Rate").pack()
rate = Entry(app)
rate.pack()

Button(app, text="Calculate", command=calculate).pack()
result = Label(app, text="")
result.pack()

app.mainloop()
