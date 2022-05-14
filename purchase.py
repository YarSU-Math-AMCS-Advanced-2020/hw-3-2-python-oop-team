from decimal import Decimal


class Purchase:
    def __init__(self, price: Decimal):
        self.price = price

    def get_price(self):
        return self.price

    def count_price(self):
        return self.price
