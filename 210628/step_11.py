class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    def show_price(self):
        print(self._price)


class NoteBook(Product):
    pass


item_1 = Product('iPhone 12 mini', 865.55)
print(type(item_1))
item_1.show_price()

item_2 = NoteBook('MacBook', 1789.11)
print(type(item_2))
item_2.show_price()
