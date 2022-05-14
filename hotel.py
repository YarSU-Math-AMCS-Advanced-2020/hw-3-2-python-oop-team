from location import Location
from decimal import Decimal


class Hotel:
    def __init__(self, title: str, price: Decimal, location: Location):
        self.title = title
        self.price = price
        self.location = location

    def print_hotel_info(self):
        print(f'{self.title}, {self.price}, {self.location.print_location()}')

    def set_title(self, title: str):
        self.title = title

    def set_title(self, price: Decimal):
        self.price = price

    def set_location(self, location: Location):
        self.location = location

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_location(self):
        return self.location

