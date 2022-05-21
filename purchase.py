from decimal import Decimal


class Purchase:
    def __init__(self, purchase_id: str, price: Decimal):
        self.purchase_id = purchase_id
        self.price = price

    def get_purchase_id(self):
        return self.purchase_id

    def get_price(self):
        return self.price

    def set_purchase_id(self, purchase_id: str):
        self.purchase_id = purchase_id

    def set_price(self, price: Decimal):
        self.price = price

    def count_price(self):
        return self.price
