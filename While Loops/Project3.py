secret_number = 69
while True:
    inp = int(input("Enter a number between 1 - 100 :"))
    if inp == secret_number:
        print("You guessed the correct number !")
        break

    else:
        print("Try again!")