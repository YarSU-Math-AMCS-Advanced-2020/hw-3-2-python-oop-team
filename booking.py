from client import Client
from decimal import Decimal
from hotel import Hotel
from ticket import Ticket
from ticket import PlainTicket
from ticket import TrainTicket
from ticket import BusTicket
import datetime
from typing import Union


class Booking:
    def __init__(self, client: Client, price: Decimal):
        self.client = client
        self.price = price


class HotelBooking(Booking):
    def __init__(self, client: Client, hotel: Hotel,
                 check_in: datetime, check_out: datetime, people_count: int):
        price = hotel.price * (check_in.days() - check_out.days()) * people_count
        super().__init__(client, price)
        self.hotel = hotel
        self.check_in = check_in
        self.check_out = check_out
        self.people_count = people_count


class TicketBooking(Booking):
    def __init__(self, client: Client,
                 ticket: Union[PlainTicket, TrainTicket, BusTicket],
                 seat: int):
        super().__init__(client, ticket.price)
        self.ticket = ticket
        self.seat = seat
