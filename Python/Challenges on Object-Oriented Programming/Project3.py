import random

class FruitQuizz:
    def __init__(self):
        self.fruits = {
            "Apple":"red",
            "Banana":"Yellow",
            "Watermelon": "green",
        }

    def quizz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}?".format(fruit))
            answer = input("Enter The Color :")

            if answer.lower() == color:
                print("Correct")
            else:
                print("Incorrect")
            
            option = input("Wanna play again (y/n):")
            if option == "n":
                break

print("Welcome to fruit quizz")

f1 = FruitQuizz()

f1.quizz()

