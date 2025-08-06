import tkinter as tk
from tkinter import messagebox
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result = ""
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"You chose {choice}\nComputer chose {computer_choice}\n\n{result}")
    
window = tk.Tk()
window.title("Rock Paper Scissors App")
window.geometry("400x400")

label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Arial", 16))
label.pack(pady=20)

rock_button = tk.Button(window, text="Rock", font=("Arial", 14), command=lambda: play("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", font=("Arial", 14), command=lambda: play("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", font=("Arial", 14), command=lambda: play("Scissors"))
scissors_button.pack(pady=10)

window.mainloop()
