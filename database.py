import json
from typing import *
from client import Client
from filters import HotelFilters, TicketFilters
from purchase import Purchase
from purchased_hotel import PurchasedHotel
from purchased_ticket import PurchasedPlaneTicket, PurchasedTrainTicket
from tour import Tour


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
        self.client_storage = ClientStorage()

    def find_hotels(self, hotel_filters: HotelFilters):
        return self.hotel_storage.find_hotels(hotel_filters)

    def find_train_tickets(self, ticket_filters: TicketFilters):
        return self.train_ticket_storage.find_train_tickets(ticket_filters)

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        return self.plane_ticket_storage.find_plane_tickets(ticket_filters)

    @staticmethod
    def add_purchased_hotel_to_client(client: Client, purchased_hotel: PurchasedHotel):
        client.add_purchased_hotel(purchased_hotel)

    @staticmethod
    def add_purchased_plane_ticket_to_client(client: Client, purchased_plane_ticket: PurchasedPlaneTicket):
        client.add_purchased_plane_ticket(purchased_plane_ticket)

    @staticmethod
    def add_purchased_train_ticket_to_client(client: Client, purchased_train_ticket: PurchasedTrainTicket):
        client.add_purchased_train_ticket(purchased_train_ticket)

    @staticmethod
    def add_tour_to_client(client: Client, tour: Tour):
        client.add_tour(tour)


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


class ClientStorage(Storage):
    def __init__(self):
        super().__init__('modified_clients.json')

    def add_purchase(self, client: Client, purchase: Purchase):
        if not self.data.get(client.client_id):
            self.data[client.client_id] = []
        self.data[client.client_id].append(purchase)

    def find_purchases(self, client: Client) -> List[Purchase]:  # Зробити фільтри
        return self.data.get(client.client_id, [])

