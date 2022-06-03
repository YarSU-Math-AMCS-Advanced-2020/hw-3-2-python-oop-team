from decimal import Decimal
from typing import Dict, Union

from purchase import Purchase

class Filters:
    def __init__(self):
        self.filter_list = []

    def is_valid(self, item: Purchase) -> bool:
        for filter in self.filter_list:
            if not filter(item):
                return False
        return True


class HotelFilters(Filters):
    def __init__(self, hotel_filters: Dict[str, Union[str, Decimal, Dict[str, str]]]):
        super().__init__()
        if hotel_filters.get('id'):
            self.filter_list.append(lambda x: x.get('id') == hotel_filters['id'])
        if hotel_filters.get('city'):
            self.filter_list.append(lambda x: x.get('location', {}).get('city') == hotel_filters['city'])
        if hotel_filters.get('country'):
            self.filter_list.append(lambda x: x.get('location', {}).get('country') == hotel_filters['country'])
        if hotel_filters.get('price'):
            self.filter_list.append(lambda x: hotel_filters['price'][0] <= x.get('price') <= hotel_filters['price'][1])


class TicketFilters(Filters):
    def __init__(self, ticket_filters: Dict[str, Union[str, Decimal]]):
        super().__init__()
        if ticket_filters.get('id'):
            self.filter_list.append(lambda x: x.get('id') == ticket_filters['id'])
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
