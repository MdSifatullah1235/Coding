class random:
    def __init__(self, a ):
        self.a = a

    def __lt__(self,other):
        if self.a < other.a:
            return "Obj 1 is lesser than Obj 2"
        
        else:
            return "Obj1 is greater than Obj 2"
        
    def __eq__(self, other):
        if self.a == other.a:
            return "Obj 1 is equal Obj 2 "
        else:
            return "Both are not equal"
        
ob1 = random(2)
ob2 = random(3)

print(ob1 == ob2)

print(ob1 > ob2)