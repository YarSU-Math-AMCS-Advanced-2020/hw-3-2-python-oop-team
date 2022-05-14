from location import Location
import datetime
from decimal import Decimal
from enum import Enum
from purchase import Purchase


class TicketType(Enum):
    plain = 1
    train = 2
    bus = 3


class PlainTicketType(Enum):
    economy = 1
    business = 2
    first = 3


class TrainTicketType(Enum):
    seat = 1
    reserved_seat = 2
    coupe = 3


class BusTicketType(Enum):
    small = 1
    medium = 2
    big = 3


class Ticket(Purchase):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal):
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.price = price

    def print_info(self):
        print(f'{self.from_location.print_location()}, {self.to_location.print_location()}, {self.departure_date},\
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


class PlainTicket(Ticket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, plain_ticket_type: PlainTicketType):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.plain_ticket_type = plain_ticket_type


class TrainTicket(Ticket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, train_ticket_type: TrainTicketType):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.train_ticket_type = train_ticket_type


class BusTicket(Ticket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, bus_ticket_type: BusTicketType):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.bus_ticket_type = bus_ticket_type
