class FlashCard:
    def __init__(self, word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + ": " + self.meaning
    

flash = []

print("FlashCard App")

while True:
    word = input("Enter the word :")
    meaning = input("Enter the meaning")

    flash.append(FlashCard(word,meaning))

    option = input("Enter some more words (y/n):")

    if option == "n":
        break


print("\n Flash cards :")

for i in flash:
    print(i)