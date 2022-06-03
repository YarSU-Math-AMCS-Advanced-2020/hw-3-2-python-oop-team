from location import Location
from purchase import Purchase

from decimal import Decimal


class Ticket(Purchase):
    def __init__(self, purchase_id: str, departure_time: str, arrival_time: str, departure_date: str,
                 arrival_date: str, duration: str, price: Decimal, from_location: str, to_location: str):
        super().__init__(purchase_id, price)
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.duration = duration
        self.from_location = from_location
        self.to_location = to_location

    def info(self):
        return f'From-location: {self.from_location}\nTo-location: {self.to_location}\n' \
               f'Departure date: {self.departure_date}\nArrival date: {self.arrival_date}\nPrice: {self.price}\n'
