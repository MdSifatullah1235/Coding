from tkinter import *

window = Tk()
window.title("Temperature Converter")
window.geometry("300x150")  

def fahrenheitToCelsius():
    """Convert the temperature from Fahrenheit to Celsius."""
    try:
        fahrenheit = float(entry_temperature.get())
        celsius = (5 / 9) * (fahrenheit - 32)
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    except ValueError:
        lbl_result["text"] = "Invalid Input!"

frame_entry = Frame(master=window)
entry_temperature = Entry(master=frame_entry, width=10)
label_temperature = Label(master=frame_entry, text="Enter temperature in °F: ")

entry_temperature.grid(row=0, column=1, sticky="w")
label_temperature.grid(row=0, column=0, sticky="e")

btn_convert = Button(
    master=window,
    text="Convert",
    command=fahrenheitToCelsius  
)
lbl_result = Label(master=window, text="\N{DEGREE CELSIUS}")

frame_entry.grid(row=0, column=0, padx=10, pady=10)
btn_convert.grid(row=1, column=0, pady=10)
lbl_result.grid(row=1, column=1, padx=10)

window.mainloop()