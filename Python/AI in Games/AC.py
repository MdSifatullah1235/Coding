import random
from colorama import Fore, init, Style
init(autoreset=True)

def display_ground(ground):
    print()

    print(Fore.GREEN + f"             Player                 ")
    print(Fore.CYAN + f"           Player chose              ")
    print("")
    print("-------------------------------")
    print(Fore.RED + f"             AI                 ")
    print(Fore.CYAN + f"           AI chose              ")
    print("")
    print("-------------------------------")