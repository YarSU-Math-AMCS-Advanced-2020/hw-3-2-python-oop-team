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


class DB:
    def __init__(self, filename: str):
        self.filename = filename
        with open(filename, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def find_hotels(self, hotel_filters: HotelFilters):
        return self.__find(self.data, hotel_filters.is_valid)

    def find_tickets(self, ticket_filters: TicketFilters):
        return self.__find(self.data, ticket_filters.is_valid)

    @staticmethod
    def __find(data: Iterable, filter_func: Callable):
        res = []
        for item in data:
            if filter_func(item):
                res.append(item)
        return res
