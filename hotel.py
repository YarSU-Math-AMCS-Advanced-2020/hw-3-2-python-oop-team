from location import Location
from purchase import Purchase

from decimal import Decimal


class Hotel(Purchase):
    def __init__(self, purchase_id: str, title: str, price: Decimal, location: Location):
        self.title = title
        self.location = location
        super().__init__(purchase_id, price)

    def info(self):
        return f'Hotel: {self.title}\nLocation: {self.location.print_location()}\nPrice: {self.price}\n'
