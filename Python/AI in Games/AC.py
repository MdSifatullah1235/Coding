import random
from colorama import Fore, init, Style
init(autoreset=True)

history = []  # to track player’s previous moves


def playground(player_choice, ai_choice):
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


def ai_move(player_choice):
    # First round strategy
    if not history:
        return "paper"  # counter common opening Rock
    
    last = history[-1]

    # If player repeated last move → counter it
    if player_choice == last:
        if player_choice == "rock":
            return "paper"
        elif player_choice == "paper":
            return "scissors"
        else:
            return "rock"

    # If player switched after losing → predict and counter
    if player_choice != last:
        if player_choice == "rock":
            return "paper"
        elif player_choice == "paper":
            return "scissors"
        else:
            return "rock"

    # Fallback: random
    return random.choice(["rock", "paper", "scissors"])


# Main game loop
while True:
    player_choice = input("\nEnter your move (rock, paper, scissors): ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print(Fore.YELLOW + "Invalid choice. Try again.")
        continue

    ai_choice = ai_move(player_choice)
    history.append(player_choice)

    playground(player_choice, ai_choice)

    # Decide winner
    if player_choice == ai_choice:
        print(Fore.YELLOW + "It's a tie!")
    elif (player_choice == "rock" and ai_choice == "scissors") or \
         (player_choice == "paper" and ai_choice == "rock") or \
         (player_choice == "scissors" and ai_choice == "paper"):
        print(Fore.GREEN + "You win!")
    else:
        print(Fore.RED + "AI wins!")

    # Ask player if they want to continue
    again = input(Fore.CYAN + "\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(Fore.MAGENTA + "\nThanks for playing! Goodbye 👋")
        break