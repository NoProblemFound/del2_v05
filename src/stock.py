class Stock:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def decrease_product(self, name, amount):
        for item in self.items:
            if item.name == name:
                item.amount -= amount