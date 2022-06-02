from decimal import Decimal
from abc import ABC


class Purchase(ABC):
    def __init__(self, purchase_id: str, price: Decimal):
        self.purchase_id = purchase_id
        self.price = price

    @staticmethod
    def is_tour():
        return False

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

    def info(self):
        return
