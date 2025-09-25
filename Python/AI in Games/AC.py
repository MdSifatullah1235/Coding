import random
from colorama import Fore, init, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    
    print(" " + colored(board[0]) + " | " + colored(board[1]) + " | " + colored(board[2]))
    print(Fore.CYAN + "-----------")
    print(" " + colored(board[3]) + " | " + colored(board[4]) + " | " + colored(board[5]))
    print(Fore.CYAN + "-----------")
    print(" " + colored(board[6]) + " | " + colored(board[7]) + " | " + colored(board[8]))
    print()

display_board(["1","2","3","4","5","6","7","8","9"])