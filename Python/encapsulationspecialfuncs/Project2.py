class Computer:
    def __init__(self):
        self.__maxprice = 250

    def sell(self):
        print("Selling Price :", self.__maxprice)

    def setmaxprice(self,price):
        self.__maxprice = price

obj = Computer()
obj.sell()

obj.__maxprice = 1000
obj.sell()

obj.setmaxprice(1500)
obj.sell()