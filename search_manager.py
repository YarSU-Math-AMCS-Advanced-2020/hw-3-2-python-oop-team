from database import DB
from filters import *


class SearchManager:
    def __init__(self):
        self.data_base = DB()

    def find_hotels(self, hotel_filters: HotelFilters):
        return self.data_base.find_hotels(hotel_filters)

    def find_train_tickets(self, ticket_filters: TicketFilters):
        return self.data_base.find_train_tickets(ticket_filters)

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        return self.data_base.find_plane_tickets(ticket_filters)
