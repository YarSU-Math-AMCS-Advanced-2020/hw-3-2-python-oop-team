from manager import Manager
from filters import TicketFilters, HotelFilters


class SearchManager(Manager):
    def __init__(self):
        super().__init__()

    def find_hotels(self, hotel_filters: HotelFilters):
        return self.data_base.find_hotels(hotel_filters)

    def find_train_tickets(self, ticket_filters: TicketFilters):
        return self.data_base.find_train_tickets(ticket_filters)

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        return self.data_base.find_plane_tickets(ticket_filters)

    def get_cities_with_hotel(self):
        return self.data_base.get_cities_from_hotel_storage()
