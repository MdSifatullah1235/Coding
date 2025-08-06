class Vehicle:
    def __init__(self, name, top_speed, mileage):
        self.name = name
        self.top_speed = top_speed
        self.mileage = mileage

    def display(self):
        print("Vehicle Name: {}, Top Speed: {}, Mileage: {}".format(self.name, self.top_speed, self.mileage))

class Bus(Vehicle):
    def __init__(self, name, top_speed, mileage, capacity):
        super().__init__(name, top_speed, mileage)
        self.capacity = capacity

    def total_fare(self):
        base_fare = self.capacity * 100
        maintenance_charge = 0.1 * base_fare
        total = base_fare + maintenance_charge
        print("Total Fare for {} passengers: {}".format(self.capacity, total))


school_bus = Bus("Volvo School Bus", 120, 10, 50)

school_bus.display()
school_bus.total_fare()