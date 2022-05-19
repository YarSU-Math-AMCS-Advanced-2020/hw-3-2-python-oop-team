import database
from hotel import Hotel
from ticket import *


class HotelFilters:
    def __init__(self, hotel_filters: dict):
        self.filter_list = []
        if hotel_filters.get('city'):
            self.filter_list.append(lambda x: x.get('location', {}).get('city') == hotel_filters['city'])
        if hotel_filters.get('country'):
            self.filter_list.append(lambda x: x.get('location', {}).get('country') == hotel_filters['country'])
        if hotel_filters.get('price'):
            self.filter_list.append(lambda x: hotel_filters['price'][0] <= x.get('price') <= hotel_filters['price'][1])

    def is_valid(self, hotel: Hotel):
        for filter in self.filter_list:
            if not filter(hotel):
                return False
        return True


class TicketFilters:
    def __init__(self, ticket_filters: dict):
        self.filter_list = []
        if ticket_filters.get('departure_time'):
            self.filter_list.append(lambda x: x.get('departure_time') == ticket_filters['departure_time'])
        if ticket_filters.get('arrival_time'):
            self.filter_list.append(lambda x: x.get('arrival_time') == ticket_filters['arrival_time'])
        if ticket_filters.get('departure_date'):
            self.filter_list.append(lambda x: x.get('departure_date') == ticket_filters['departure_date'])
        if ticket_filters.get('arrival_time'):
            self.filter_list.append(lambda x: x.get('arrival_date') == ticket_filters['arrival_date'])
        if ticket_filters.get('duration'):
            self.filter_list.append(lambda x: x.get('duration') == ticket_filters['duration'])
        if ticket_filters.get('price'):
            self.filter_list.append(
                lambda x: ticket_filters['price'][0] <= x.get('price') <= ticket_filters['price'][1])
        if ticket_filters.get('from'):
            self.filter_list.append(lambda x: x.get('from') == ticket_filters['from'])
        if ticket_filters.get('to'):
            self.filter_list.append(lambda x: x.get('to') == ticket_filters['to'])

    def is_valid(self, ticket: Ticket):
        for filter in self.filter_list:
            if not filter(ticket):
                return False
        return True
