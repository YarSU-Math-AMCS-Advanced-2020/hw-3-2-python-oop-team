from booking import Booking, TicketBooking, HotelBooking
from client import Client
from hotel import Hotel
from location import Location
from ticket import Ticket, PlainTicket, TrainTicket, BusTicket
from enum import Enum
import datetime
from decimal import Decimal


class OperationType(Enum):
    none = 0
    ticket = 1
    hotel = 2


class TravelManager:
    def __init__(self):
        self.type = OperationType.none
        self.current_client = Client()

    def set_type(self, operation_type: OperationType):
        self.type = operation_type

    def ticket_searching(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal):
        return
        # TODO: this function

    def ticket_purchase_creation(self, chosen_ticket: Ticket, chosen_seat: int):
        new_ticket_booking = TicketBooking(self.current_client, chosen_ticket, chosen_seat)
        return new_ticket_booking


    class BookingFactory:
        def create_booking(operation_type: OperationType):
            booking = None
            # TODO: to do


