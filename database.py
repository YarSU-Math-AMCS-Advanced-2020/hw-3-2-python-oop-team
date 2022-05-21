import json
from typing import *
from filters import *
from client import *
from purchased_ticket import *


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton.__instance:
            Singleton.__instance[cls] = cls.__new__(cls)
            Singleton.__instance[cls].__init__(*args, **kwargs)
        return Singleton.__instance[cls]


class DB(metaclass=Singleton):
    def __init__(self):
        self.hotel_data = HotelStorage()
        self.train_ticket_data = TrainTicketStorage()
        self.plane_ticket_data = PlaneTicketStorage()

    def find_hotels(self, hotel_filters: HotelFilters):
        return self.__find(self.hotel_data.get_content(), hotel_filters.is_valid)

    def find_train_tickets(self, ticket_filters: TicketFilters):
        return self.__find(self.train_ticket_data.get_content(), ticket_filters.is_valid)

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        return self.__find(self.plane_ticket_data.get_content(), ticket_filters.is_valid)

    @staticmethod
    def __find(data: Iterable, filter_func: Callable):
        res = []
        for item in data:
            if filter_func(item):
                res.append(item)
        return res

    @staticmethod
    def add_purchased_hotel_to_client(client: Client, purchased_hotel: PurchasedHotel):
        client.add_purchased_hotel(purchased_hotel)

    @staticmethod
    def add_purchased_plane_ticket_to_client(client: Client, purchased_plane_ticket: PurchasedPlaneTicket):
        client.add_purchased_plane_ticket(purchased_plane_ticket)

    @staticmethod
    def add_purchased_train_ticket_to_client(client: Client, purchased_train_ticket: PurchasedTrainTicket):
        client.add_purchased_train_ticket(purchased_train_ticket)


class Storage:
    def __init__(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def get_content(self):
        res = []
        for item in self.data:
            res.append(item)
        return res


class HotelStorage(Storage):
    def __init__(self):
        super().__init__('modified_hotels.json')


class TrainTicketStorage(Storage):
    def __init__(self):
        super().__init__('modified_train_tickets.json')


class PlaneTicketStorage(Storage):
    def __init__(self):
        super().__init__('modified_plane_tickets.json')
