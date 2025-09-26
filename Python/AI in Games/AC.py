import random
from colorama import Fore, init, Style
init(autoreset=True)

player_choice = input("Enter your move (rock, paper, scissors): ").lower()

history = []

def playground(ai_choice):
    print()
    print(Fore.GREEN + "--- Player ---")
    print(Fore.CYAN + f"Player chose {player_choice}")
    if player_choice == "rock":
        print(Fore.GREEN + """
    _______
---'   ____ )
      (_____ )
      (_____ )
      (____ )
---.__(___ )
""")
    elif player_choice == "paper":
        print(Fore.GREEN + """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif player_choice == "scissors":
        print(Fore.GREEN + """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    print()
    print("----------------------------")
    print()
    print(Fore.CYAN + f"AI chose {ai_choice}")
    if ai_choice == "rock":
        print(Fore.RED + """
    _______
---'   ____ )
      (_____ )
      (_____ )
      (____ )
---.__(___ )
""")
    elif ai_choice == "paper":
        print(Fore.RED + """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif ai_choice == "scissors":
        print(Fore.RED + """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    print(Fore.RED + "--- AI ---")


def ai_move():
    if not history:  
        return "paper"
    else:
        last = history[-1]

        if (last == "rock" and player_choice == "rock") or \
           (last == "paper" and player_choice == "paper") or \
           (last == "scissors" and player_choice == "scissors"):
            if player_choice == "rock":
                return "paper"
            elif player_choice == "paper":
                return "scissors"
            else:
                return "rock"

        if last != player_choice:
            if player_choice == "rock":
                return "paper"
            elif player_choice == "paper":
                return "scissors"
            else:
                return "rock"

        return random.choice(["rock", "paper", "scissors"])


ai_choice = ai_move()
history.append(player_choice)
playground(ai_choice)

if player_choice == ai_choice:
    print(Fore.YELLOW + "It's a tie!")
elif (player_choice == "rock" and ai_choice == "scissors") or \
     (player_choice == "paper" and ai_choice == "rock") or \
     (player_choice == "scissors" and ai_choice == "paper"):
    print(Fore.GREEN + "You win!")
else:
    print(Fore.RED + "AI wins!")
