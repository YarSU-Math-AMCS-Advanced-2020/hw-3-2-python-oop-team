from location import Location
from decimal import Decimal
from enum import Enum
from purchase import Purchase
import datetime


class Ticket(Purchase):
    def __init__(self, purchase_id: str, departure_time: datetime, arrival_time: datetime, departure_date: datetime,
                 arrival_date: datetime, duration: str, price: Decimal, from_location: str, to_location: str):
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

    def set_departure_time(self, departure_time: datetime):
        self.departure_time = departure_time

    def set_arrival_time(self, arrival_time: datetime):
        self.arrival_time = arrival_time

    def set_departure_date(self, departure_date: datetime):
        self.departure_date = departure_date

    def set_arrival_date(self, arrival_date: datetime):
        self.arrival_date = arrival_date

    def set_duration(self, duration: datetime):
        self.duration = duration

    def set_from_location(self, from_location: Location):
        self.from_location = from_location

    def set_to_location(self, to_location: Location):
        self.from_location = to_location
