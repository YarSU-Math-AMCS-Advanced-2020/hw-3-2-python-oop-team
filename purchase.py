from decimal import Decimal


class Purchase:
    def __init__(self, purchase_id: str, price: Decimal):
        self.purchased_id = purchase_id
        self.price = price

    def get_price(self):
        return self.price

    def count_price(self):
        return self.price
