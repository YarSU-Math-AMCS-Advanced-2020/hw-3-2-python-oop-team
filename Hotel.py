import Location
from decimal import Decimal


class Hotel:
    def __init__(self, location: Location, price: Decimal):
        self.location = location
        self.price = price
    # TODO: print hotel info
