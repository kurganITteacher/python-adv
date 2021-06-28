class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


item_1 = Product('iPhone 12 mini', 865.55)
print(item_1.price)
item_1.price = '568 rub'
# item_1.price = 568
print(item_1.price)

item_2 = Product('iPad', 789.11)
print(item_1.price + item_2.price)

