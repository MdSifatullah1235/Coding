class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("A Bird")

    def run(self):
        print("Run faster")
    
    def fly(self):
        print("Fly faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__() 
        print("Penguin is ready")

    def whoisthis(self):
        print("A Penguin")
    
    def run(self):
        print("Penguins run faster")

    def fly(self):
        print("Penguins can't fly, but they swim!")

p1 = Penguin()

p1.whoisthis()
p1.run()
p1.fly()