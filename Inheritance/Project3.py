class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
        print("A Bird")

    def run(self):
        print("run faster")
    
    def fly(self):
        print("Fly faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin Is Ready")

    def whoisthis(self):
        print("A Penguin")
    
    def run(self):
        print("Run Faster")

    def fly(self):
        print("fly faster")

p1 = Penguin()

p1.whoisthis()