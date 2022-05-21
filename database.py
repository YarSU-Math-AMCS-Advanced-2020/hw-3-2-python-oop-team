import json
from typing import *
from filters import *


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton.__instance:
            Singleton.__instance[cls] = cls.__new__(cls)
            Singleton.__instance[cls].__init__(*args, **kwargs)
        return Singleton.__instance[cls]


class DB(metaclass=Singleton):
    def __init__(self):
        self.hotel_storage = HotelStorage()
        self.train_ticket_storage = TrainTicketStorage()
        self.plane_ticket_storage = PlaneTicketStorage()

    def find_hotels(self, hotel_filters: HotelFilters):
        return self.hotel_storage.find_hotels(hotel_filters)

    def find_train_tickets(self, ticket_filters: TicketFilters):
        self.train_ticket_storage.find_train_tickets(ticket_filters)

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        self.plane_ticket_storage.find_plane_tickets(ticket_filters)


class Storage:
    def __init__(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def get_content(self) -> List[Purchase]:
        return self.data

    @staticmethod
    def find(data: Iterable, filter_func: Callable):
        res = []
        for item in data:
            if filter_func(item):
                res.append(item)
        return res


class HotelStorage(Storage):
    def __init__(self):
        super().__init__('modified_hotels.json')

    def find_hotels(self, hotel_filters: HotelFilters):
        return HotelStorage.find(self.data, hotel_filters.is_valid)


class TrainTicketStorage(Storage):
    def __init__(self):
        super().__init__('modified_train_tickets.json')

    def find_train_tickets(self, ticket_filters: TicketFilters):
        return TrainTicketStorage.find(self.data, ticket_filters.is_valid)


class PlaneTicketStorage(Storage):
    def __init__(self):
        super().__init__('modified_plane_tickets.json')

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        return PlaneTicketStorage.find(self.data, ticket_filters.is_valid)
