class BMW:
    def speed(self):
        print("BMW: 240 km/h")
    
    def engine(self):
        print("Engine: M30")

class Ferrari:
    def speed(self):
        print("Ferrari: 350 km/h")
    
    def engine(self):
        print("Engine: V12")

bmw = BMW()
ferrari = Ferrari()

for cars in (bmw,ferrari):
    cars.speed()
    cars.engine()