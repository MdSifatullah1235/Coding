class Parrot:
    species  = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
blu = Parrot("Blu",25)
par = Parrot("Par",35)

print("Blu is a {}".format(blu.species))
print("Par is a {}".format(par.species))

print("Name : {}, Age : {}".format(blu.name,blu.age))