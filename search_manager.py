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

    def get_train_departure_cities(self):
        return self.data_base.get_departure_cities_from_train_storage()

    def get_train_arrival_cities(self):
        return self.data_base.get_arrival_cities_from_train_storage()

    def get_train_arrival_cities_by_departure(self, ticket_filters: TicketFilters):
        return self.data_base.get_arrival_cities_by_departure_from_train_storage(ticket_filters)

    def get_plane_departure_cities(self):
        return self.data_base.get_departure_cities_from_plane_storage()

    def get_plane_arrival_cities(self):
        return self.data_base.get_arrival_cities_from_plane_storage()

    def get_plane_arrival_cities_by_departure(self, ticket_filters: TicketFilters):
        return self.data_base.get_arrival_cities_by_departure_from_plane_storage(ticket_filters)
