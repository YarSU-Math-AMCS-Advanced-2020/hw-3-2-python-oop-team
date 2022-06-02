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

    def print_info(self):
        print(f'{self.from_location}, {self.to_location}, {self.departure_date},\
        {self.arrival_date}, {self.price}')

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_departure_date(self):
        return self.departure_date

    def get_arrival_date(self):
        return self.arrival_date

    def get_duration(self):
        return self.duration

    def get_from_location(self):
        return self.from_location

    def get_to_location(self):
        return self.to_location

    def set_departure_time(self, departure_time: str):
        self.departure_time = departure_time

    def set_arrival_time(self, arrival_time: str):
        self.arrival_time = arrival_time

    def set_departure_date(self, departure_date: str):
        self.departure_date = departure_date

    def set_arrival_date(self, arrival_date: str):
        self.arrival_date = arrival_date

    def set_duration(self, duration: str):
        self.duration = duration

    def set_from_location(self, from_location: Location):
        self.from_location = from_location

    def set_to_location(self, to_location: Location):
        self.from_location = to_location

    def info(self):
        return f'From-location: {self.from_location}\nTo-location: {self.to_location}\n' \
               f'Departure date: {self.departure_date}\nArrival date: {self.arrival_date}\nPrice: {self.price}\n'
