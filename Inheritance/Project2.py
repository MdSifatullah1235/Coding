class Person:
    def __init__(self,name , age):
        self.name = name 
        self.age = age
    
    def display(self):
        print("Name :",self.name,"Age :",self.age)

    
class Employee(Person):
    def __init__(self, name, age,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,age)
    
    def display(self):
        print("Name :",self.name,"Age :",self.age,"Salary :",self.salary,"Post :",self.post)

e1 = Employee("Micheal",20,80000,"HR")
e1.display()