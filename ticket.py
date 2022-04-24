from location import Location
import datetime
from decimal import Decimal
from enum import Enum


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


class Ticket:
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal):
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.price = price
    # TODO: print_info(for ticket)


class PlainTicket(Ticket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, plain_ticket_type: PlainTicketType):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.plain_ticket_type = plain_ticket_type
    # TODO: changing print_info for plain_ticket


class TrainTicket(Ticket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, train_ticket_type: TrainTicketType):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.train_ticket_type = train_ticket_type
    # TODO: changing print_info for train_ticket


class BusTicket(Ticket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, bus_ticket_type: BusTicketType):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.bus_ticket_type = bus_ticket_type
    # TODO: changing print_info for bus_ticket
