import random

wins = 0
loses = 0

while True:
    user_choice = input("Enter a choice (rock/paper/scissors): ")

    choices = ["rock", "paper", "scissors"]
    sys_choice = random.choice(choices)
    print(f"You chose {user_choice}. System chose {sys_choice}.")

    if user_choice == sys_choice:
        print(f"You both chose {user_choice}. It's a tie!")

    elif user_choice == "rock":
        if sys_choice == "scissors":
            print("Rock beats Scissors. You win!")
            wins += 1
        else:
            print("Paper beats Rock. You lose!")
            loses += 1

    elif user_choice == "paper":
        if sys_choice == "rock":
            print("Paper beats Rock. You win!")
            wins += 1
        else:
            print("Scissors beat Paper. You lose!")
            loses += 1

    elif user_choice == "scissors":
        if sys_choice == "paper":
            print("Scissors beat Paper. You win!")
            wins += 1
        else:
            print("Rock beats Scissors. You lose!")
            loses += 1

    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    play_again = input("Wanna play again (y/n): ")
    if play_again == "n":
        print("Oh... okay.")
        print(f"You won {wins} times.")
        print(f"You lost {loses} times.")
        if wins >= 5 and loses == 0:
            print("You are so lucky")
        break
    else:
        print("Let's play again!")