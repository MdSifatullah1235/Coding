import random

play = True
guess = str(random.randint(10,20))

print("I will generate a number from 10 to 20 Try to guess it!")
print("A secret",guess)
while play:
    number = input("Enter a number:")
    if number == guess:
        print("You guessed it!")
        print("The Number Was",number)
        break
    else:
        print("Try Again")
