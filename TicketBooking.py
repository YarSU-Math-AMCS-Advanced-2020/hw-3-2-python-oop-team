import Ticket
import Client
from decimal import Decimal


class TicketBooking:
    def __init__(self, client: Client, ticket: Ticket, seat: int, price: Decimal):
        self.client = client
        self.ticket = ticket
        self.seat = seat
        self.price = ticket.price
