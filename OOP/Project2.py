class Vehicle:
    cls = "Vehicle"
    def __init__(self,model,color,top_speed):
        self.model = model
        self.color = color
        self.top_speed = top_speed

obj = Vehicle("F6","Red",269)

print("Model :",obj.model,"\nColor :",obj.color,"\nTop Speed :",obj.top_speed)