from client import Client
from filters import HotelFilters, TicketFilters
from purchase import Purchase
from tour import Tour

import json
from typing import List, Iterable, Callable


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
        self.tour_storage = TourStorage()

    def find_hotels(self, hotel_filters: HotelFilters):
        return self.hotel_storage.find_hotels(hotel_filters)

    def find_train_tickets(self, ticket_filters: TicketFilters):
        return self.train_ticket_storage.find_train_tickets(ticket_filters)

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        return self.plane_ticket_storage.find_plane_tickets(ticket_filters)

    def add_purchase(self, client: Client, purchase: Purchase):
        self.client_storage.add_purchase(client, purchase)

    def find_purchases(self, client: Client):
        return self.client_storage.find_purchases(client)

    def add_purchase_to_tour(self, tour: Tour, purchase: Purchase):
        self.tour_storage.add_purchase(tour, purchase)


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
        return self.data.get(client.client_id)


class TourStorage(Storage):
    def __init__(self):
        super().__init__('modified_tours.json')

    def add_tour(self, tour: Tour):
        if not self.data.get(tour.purchase_id):
            self.data[tour.purchase_id] = tour

    def add_purchase(self, tour: Tour, purchase: Purchase):
        if not self.data.get(tour.purchase_id):
            self.data[tour.purchase_id] = tour
        self.data[tour.purchase_id].add_purchase(purchase)

    def find_tour(self, tour: Tour):
        return self.data.get(tour.purchase_id)

