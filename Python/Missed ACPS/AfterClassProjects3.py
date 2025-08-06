class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        pi = 3.14159
        return pi * self.radius ** 2

    def compute_perimeter(self):
        pi = 3.14159
        return 2 * pi * self.radius

circle = Circle(5)

print("Area of the circle: {:.2f}".format(circle.compute_area()))
print("Perimeter of the circle: {:.2f}".format(circle.compute_perimeter()))