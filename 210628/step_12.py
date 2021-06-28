class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    # def price(self):
    #     return self._price

    @property
    def price(self):
        return self._price

    # @price.setter
    # def price(self, val):
    #     self._price = float(val)


item_1 = Product('iPhone 12 mini', 865.55)
print(item_1.price)
# item_1.price = '568 rub'
item_1.price = '568'
# item_1._price = '568 rub'
# item_1.Product__price = '568 rub'
# print(item_1.price)

item_2 = Product('iPad', 789.11)
print(item_1.price + item_2.price)
