import Location
import datetime
from decimal import Decimal
import enum


class Ticket:
    class TicketType(enum.Enum):
        plain = 1
        train = 2
        bus = 3

    def __init__(self, from_location: Location, to_location: Location, duration: datetime,
                 price: Decimal, ticket_type: TicketType):
        self.from_location = from_location
        self.to_location = to_location
        self.duration = duration
        self.price = price
        self.ticket_type = ticket_type
