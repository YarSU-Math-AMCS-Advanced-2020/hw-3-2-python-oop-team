from decimal import Decimal
from abc import ABC


class Purchase(ABC):
    def __init__(self, purchase_id: str, price: Decimal):
        self.purchase_id = purchase_id
        self.price = price

    @staticmethod
    def is_tour():
        return False

    def count_price(self):
        return self.price

    def info(self):
        return
