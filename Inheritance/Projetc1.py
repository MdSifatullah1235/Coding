class Vehicle:
    def __init__(self,name,top_speed,mileage):
        self.name = name
        self.top_speed = top_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

v1 = Vehicle("Buggati Chiron",250,15)
school_bus = Bus("Volvo",200,15)

print("Vehicle Name :", v1.name,"Top Speed :",v1.top_speed,"Mileage :",v1.mileage)

print("Bus Name :",school_bus.name,"Top Speed :",school_bus.top_speed,"Mileage :",school_bus.mileage)