class computer:
    def __init__(self):
        self.__maxprice = 80000
    def sell(self):
        print("Selling Price: ",self.__maxprice)
    def setMaxPrice(self,price):
        self.__maxprice = price

c = computer()
c.sell()
c.maxprice = 100000
c.sell()
c.setMaxPrice(90000)
c.sell()


