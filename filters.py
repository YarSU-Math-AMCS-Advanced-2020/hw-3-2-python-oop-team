from decimal import Decimal
from typing import Dict, Union, Tuple

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
    def __init__(self, hotel_filters: Dict[str, Union[str, Decimal, Dict[str, str], Tuple[Decimal]]]):
        super().__init__()
        if 'id' in hotel_filters:
            self.filter_list.append(lambda x: x.get('id') == hotel_filters['id'])
        if 'city' in hotel_filters:
            self.filter_list.append(lambda x: x.get('location', {}).get('city') == hotel_filters['city'])
        if 'country' in hotel_filters:
            self.filter_list.append(lambda x: x.get('location', {}).get('country') == hotel_filters['country'])
        if 'price' in hotel_filters:
            self.filter_list.append(lambda x: hotel_filters['price'][0] <= x.get('price') <= hotel_filters['price'][1])


class TicketFilters(Filters):
    def __init__(self, ticket_filters: Dict[str, Union[str, Decimal, Tuple[Decimal]]]):
        super().__init__()
        if 'id' in ticket_filters:
            self.filter_list.append(lambda x: x.get('id') == ticket_filters['id'])
        if 'departure_time' in ticket_filters:
            self.filter_list.append(lambda x: x.get('departure_time') == ticket_filters['departure_time'])
        if 'arrival_time' in ticket_filters:
            self.filter_list.append(lambda x: x.get('arrival_time') == ticket_filters['arrival_time'])
        if 'departure_date' in ticket_filters:
            self.filter_list.append(lambda x: x.get('departure_date') == ticket_filters['departure_date'])
        if 'arrival_date' in ticket_filters:
            self.filter_list.append(lambda x: x.get('arrival_date') == ticket_filters['arrival_date'])
        if 'duration' in ticket_filters:
            self.filter_list.append(lambda x: x.get('duration') == ticket_filters['duration'])
        if 'price' in ticket_filters:
            self.filter_list.append(
                lambda x: ticket_filters['price'][0] <= x.get('price') <= ticket_filters['price'][1])
        if 'from' in ticket_filters:
            self.filter_list.append(lambda x: x.get('from') == ticket_filters['from'])
        if 'to' in ticket_filters:
            self.filter_list.append(lambda x: x.get('to') == ticket_filters['to'])
