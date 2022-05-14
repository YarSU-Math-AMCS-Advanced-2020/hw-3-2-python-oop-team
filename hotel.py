from location import Location
from decimal import Decimal
from purchase import Purchase


class Hotel(Purchase):
    def __init__(self, title: str, price: Decimal, location: Location):
        self.title = title
        self.price = price
        self.location = location

    def print_hotel_info(self):
        print(f'{self.title}, {self.price}, {self.location.print_location()}')

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_location(self):
        return self.location
