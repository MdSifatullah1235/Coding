from tkinter import *

window = Tk()
window.title("Length Converter")
window.geometry("300x150")

def inches_to_centimeter():
    try:
        inch = float(entry_length.get())
        centimeter = inch * 2.54
        lbl_result["text"] = f"{round(centimeter, 2)} cm"
    except ValueError:
        lbl_result["text"] = "Invalid Input!"

frame_entry = Frame(master=window)
entry_length = Entry(master=frame_entry, width=10)
label_length = Label(master=frame_entry, text="Enter The Length In Inches :")

entry_length.grid(row=0, column=1, sticky="w")
label_length.grid(row=0, column=0, sticky="e")

btn_convert = Button(
    master=window,
    text="Convert",
    command=inches_to_centimeter
)

lbl_result = Label(master=window, text="cm")

frame_entry.grid(row=0, column=0, padx=10, pady=10)
btn_convert.grid(row=1, column=0, pady=10)
lbl_result.grid(row=1, column=1, padx=10)

window.mainloop()