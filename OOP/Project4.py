class StringIO():
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = input("Enter a string :")
    
    def result(self):
        print("Converted String :",self.str1.upper())

obj = StringIO()
obj.getString()
obj.result()