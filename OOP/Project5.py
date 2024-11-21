class Employee():
    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Employee Deleted")

def create_obj():
    print("Creating Object")
    obj = Employee()
    return obj

print("Calling create_obj function")
obj = create_obj()
print("Program Ending")