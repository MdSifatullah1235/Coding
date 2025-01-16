import tkinter as tk
from tkinter import messagebox

class restuarantmangement:
    def __init__(self, window):
        self.window = window
        self.window.title("Restuarant Management")

        self_menuitems = {
            "Burrito":10,
            "Pizza":25,
            "Donuts":5,
            "Noodles":20
        }
        self.exchange_rates = 120
        self.setupbackgorund(window)

        frame = tk.Frame(window)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        tk.Label(frame,text="Restuarant Management").grid(row=0,columnspan=3,padx=10,pady=10)

        self.menu_label = {}
        self.menu_quantity = {}