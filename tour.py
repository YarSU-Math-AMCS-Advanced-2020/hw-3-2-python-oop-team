from purchase import Purchase
from decimal import Decimal


class Tour(Purchase):
    def __init__(self, purchase_id: str):
        # Айди задаётся в конструкторе тура, изначальная цена - 0
        super().__init__(purchase_id, Decimal(0))
        self.purchase_list = []

    @staticmethod
    def is_tour():
        return True

    def get_purchase_list(self):
        purchase_list_copy = self.purchase_list.copy()
        return purchase_list_copy

    def count_price(self):
        price_sum = 0.0
        for i in self.purchase_list:
            price_sum += i
        return price_sum

    def add_purchase(self, purchase: Purchase):
        self.purchase_list.append(purchase)

    def info(self):
        info_string = ''
        for purchase_object in self.purchase_list:
            info_string = f'{info_string}{purchase_object.info()}\n'
        return info_string
