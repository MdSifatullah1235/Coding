class Dog:
    species = "Canis Familiaris"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def display_details(self):
        print("Breed: {}".format(self.breed))
        print("Color: {}".format(self.color))
        print("Species: {}".format(Dog.species))

dog1 = Dog("Labrador Retriever", "Yellow")
dog2 = Dog("German Shepherd", "Black and Tan")
print(dog1)
print(dog2)