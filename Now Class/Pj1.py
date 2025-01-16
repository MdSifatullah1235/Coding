import tkinter as tk
from tkinter import messagebox , ttk
class restuarantmangement:
    def __init__(self, window):
        self.window = window
        self.window.title("Restuarant Management")

        self.menuitems = {
            "Burrito":10,
            "Pizza":25,
            "Donuts":5,
            "Noodles":20
        }
        self.exchange_rates = 120
        self.setupbackgorund(window)

        frame = ttk.Frame(window)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        ttk.Label(frame,text="Restuarant Management").grid(row=0,columnspan=3,padx=10,pady=10)

        self.menu_label = {}
        self.menu_quantity = {}

        for i,(item,price) in enumerate(self.menuitems.items(),start=1):
            label = ttk.Label(frame,text=f"{item} (${price}) ", font=("Arial",12))
            quantity_entry = tk.Entry(frame,width=5)

        self.currencyvar = tk.StringVar()
        ttk.Label(frame,text="Currency",font=("Arial",12)).grid(row= len(self.menuitems) + 1, padx=10,pady=10,column=0)

        currency_dropdown = ttk.Combobox(frame,textvariable=self.currencyvar, values=["USD","BDT"])

        currency_dropdown.grid(row= len(self.menuitems) + 1, padx=10,pady=10,column=1)
        currency_dropdown.current(0)

