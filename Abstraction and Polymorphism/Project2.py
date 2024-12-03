from abc import ABC, abstractmethod

class Animal:
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("Human Walks")

class Snake(Animal):
    def move(self):
        print("Snak Bites")

class Lion(Animal):
    def move(self):
        print("Lion Roars")

class Dog(Animal):
    def move(self):
        print("Dog Barks")

h1 = Human()
s1 = Snake()
l1 = Lion()
d1 = Dog()

h1.move()
s1.move()
l1.move()
d1.move()