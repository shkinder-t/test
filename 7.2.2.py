class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self.__number = number
        self.place(number)

    def place(self, prum):
        if prum < 0:
            print("out of stock")
        elif 0 < prum < 100:
            print("warehouse")
        else:
            print("Remote warehouse")

    def plus(self, pls_num):
        self.__number += pls_num
        self.place(self.__number)

    def minus(self, min_num):
        self.__number -= min_num
        self.place(self.__number)

    def inform(self):
        print(self.material, self.color, self.__number)

    def getnuber(self):
        return self.__number

class Market(Building):
    def __init__(self, material, color, price, number=0):
        super().__init__(material, color, number=number)
        self.price = price
    def info(self):
        print(self.material, self.color, self.getnuber(), self.price)


brick = Market("brick", "white", 85.26, 300)
plank = Market("plank", "brown", 54.49, 20)

brick.info()

brick.plus(50)
plank.minus(3)

brick.info()
print(brick.material)

