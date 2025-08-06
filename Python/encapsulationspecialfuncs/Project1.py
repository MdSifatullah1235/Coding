class MyClass:
    __privateVar = 20
    def __private(self):
        print("This is a private  method")
    def public(self):
        print("This is a public Method")

obj = MyClass()
obj.__private()
obj.public()
