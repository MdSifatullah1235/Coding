from tkinter import *
window = Tk()
window.geometry("100x100")
window.title("Event Handler")

def handle_keypress(event):
    print(f"Key Pressed {event.char}")

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print(f"\n Button Is Clicked")


button = Button(text="Click Me")

button.pack()
button.bind("Button-1",handle_click)

window.mainloop()
