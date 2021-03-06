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
        if purchase.is_tour():
            self.client_storage.add_purchase(client, self.tour_storage.data[purchase.purchase_id])
        else:
            self.client_storage.add_purchase(client, purchase)

    def find_client_purchases(self, client: Client):
        return self.client_storage.find_purchases(client)

    def add_purchase_to_tour(self, tour: Tour, purchase: Purchase):
        self.tour_storage.add_purchase(tour, purchase)

    def find_tour(self, tour: Tour):
        return self.tour_storage.find_tour(tour)

    def get_cities_from_hotel_storage(self):
        return self.hotel_storage.get_cities()

    def get_departure_cities_from_train_storage(self):
        return self.train_ticket_storage.get_departure_cities()

    def get_arrival_cities_from_train_storage(self):
        return self.train_ticket_storage.get_arrival_cities()

    def get_arrival_cities_by_departure_from_train_storage(self, ticket_filters: TicketFilters):
        return self.train_ticket_storage.get_arrival_cities_by_departure(ticket_filters)

    def get_departure_cities_from_plane_storage(self):
        return self.plane_ticket_storage.get_departure_cities()

    def get_arrival_cities_from_plane_storage(self):
        return self.plane_ticket_storage.get_departure_cities()

    def get_arrival_cities_by_departure_from_plane_storage(self, ticket_filters: TicketFilters):
        return self.plane_ticket_storage.get_arrival_cities_by_departure(ticket_filters)


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
        super().__init__(r'data\modified_hotels.json')

    def find_hotels(self, hotel_filters: HotelFilters):
        return HotelStorage.find(self.data, hotel_filters.is_valid)

    def get_cities(self):
        cities = []
        for item in self.data:
            cities.append(item['location']['city'])
        return list(set(cities))


class TrainTicketStorage(Storage):
    def __init__(self):
        super().__init__(r'data\modified_train_tickets.json')

    def find_train_tickets(self, ticket_filters: TicketFilters):
        return self.find(self.data, ticket_filters.is_valid)

    def get_departure_cities(self):
        cities = []
        for item in self.data:
            cities.append(item['from'])
        return list(set(cities))

    def get_arrival_cities(self):
        cities = []
        for item in self.data:
            cities.append(item['to'])
        return list(set(cities))

    def get_arrival_cities_by_departure(self, ticket_filters: TicketFilters):
        cities = []
        targets = self.find(self.data, ticket_filters.is_valid)
        for item in targets:
            cities.append(item['to'])
        return list(set(cities))


class PlaneTicketStorage(Storage):
    def __init__(self):
        super().__init__(r'data\modified_plane_tickets.json')

    def find_plane_tickets(self, ticket_filters: TicketFilters):
        return self.find(self.data, ticket_filters.is_valid)

    def get_departure_cities(self):
        cities = []
        for item in self.data:
            cities.append(item['from'])
        return list(set(cities))

    def get_arrival_cities(self):
        cities = []
        for item in self.data:
            cities.append(item['to'])
        return list(set(cities))

    def get_arrival_cities_by_departure(self, ticket_filters: TicketFilters):
        cities = []
        targets = self.find(self.data, ticket_filters.is_valid)
        for item in targets:
            cities.append(item['to'])
        return list(set(cities))


class ClientStorage(Storage):
    def __init__(self):
        super().__init__(r'data\modified_clients.json')

    def add_purchase(self, client: Client, purchase: Purchase):
        if not self.data.get(client.client_id):
            self.data[client.client_id] = []
        self.data[client.client_id].append(purchase)

    def find_purchases(self, client: Client) -> List[Purchase]:  # ?????????????? ??????????????
        return self.data.get(client.client_id)


class TourStorage(Storage):
    def __init__(self):
        super().__init__(r'data\modified_tours.json')

    def add_tour(self, tour: Tour):
        if not self.data.get(tour.purchase_id):
            self.data[tour.purchase_id] = tour

    def add_purchase(self, tour: Tour, purchase: Purchase):
        if not self.data.get(tour.purchase_id):
            self.data[tour.purchase_id] = tour
        self.data[tour.purchase_id].add_purchase(purchase)

    def find_tour(self, tour: Tour):
        return self.data.get(tour.purchase_id)
