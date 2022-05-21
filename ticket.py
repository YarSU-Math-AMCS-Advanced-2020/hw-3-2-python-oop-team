from location import Location
from decimal import Decimal
from enum import Enum
from purchase import Purchase
import datetime

class Ticket(Purchase):
    def __init__(self, purchase_id: str, departure_time: datetime, arrival_time: datetime, departure_date: datetime,
                 arrival_date: datetime, price: Decimal, from_location: str, to_location: str):
        super().__init__(purchase_id, price)
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.from_location = from_location
        self.to_location = to_location

    def print_info(self):
        print(f'{self.from_location}, {self.to_location}, {self.departure_date},\
        {self.arrival_date}, {self.price}')

    def get_from_location(self):
        return self.from_location

    def get_to_location(self):
        return self.to_location

    def get_departure_date(self):
        return self.departure_date

    def get_arrival_date(self):
        return self.arrival_date

    def get_price(self):
        return self.price

    def set_from_location(self, from_location: Location):
        self.from_location = from_location

    def set_to_location(self, to_location: Location):
        self.from_location = to_location

    def set_departure_date(self, departure_date: datetime):
        self.departure_date = departure_date

    def set_arrival_date(self, arrival_date: datetime):
        self.arrival_date = arrival_date

    def set_price(self, price: Decimal):
        self.price = price


# class TicketType(Enum):
#     plane = 1
#     train = 2
#     bus = 3
#
#
# class PlaneTicketType(Enum):
#     economy = 1
#     business = 2
#     first = 3
#
#
# class TrainTicketType(Enum):
#     seat = 1
#     reserved_seat = 2
#     coupe = 3
#
#
# class BusTicketType(Enum):
#     small = 1
#     medium = 2
#     big = 3


# class PlaneTicket(Ticket):
#     def __init__(self, departure_time: datetime, arrival_time: datetime, departure_date: datetime,
#                  arrival_date: datetime, price: Decimal, from_location: str, to_location: str,
#                  plane_ticket_type: PlaneTicketType):
#         super().__init__(departure_time, arrival_time, departure_date, arrival_date, price, from_location, to_location)
#         self.plane_ticket_type = plane_ticket_type
#
#
# class TrainTicket(Ticket):
#     def __init__(self, departure_time: datetime, arrival_time: datetime, departure_date: datetime,
#                  arrival_date: datetime, price: Decimal, from_location: str, to_location: str,
#                  train_ticket_type: TrainTicketType):
#         super().__init__(departure_time, arrival_time, departure_date, arrival_date, price, from_location, to_location)
#         self.train_ticket_type = train_ticket_type
#
#
# class BusTicket(Ticket):
#     def __init__(self, departure_time: datetime, arrival_time: datetime, departure_date: datetime,
#                  arrival_date: datetime, price: Decimal, from_location: str, to_location: str,
#                  bus_ticket_type: BusTicketType):
#         super().__init__(departure_time, arrival_time, departure_date, arrival_date, price, from_location, to_location)
#         self.bus_ticket_type = bus_ticket_type
