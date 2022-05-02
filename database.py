import json
import pandas as pd
from typing import *


class DB:
    def __init__(self, filename: str):
        self.filename = filename
        with open(filename, 'r') as file:
            self.data = json.load(file)

    def find_hotels(self, filters: dict):
        filters_list = []
        res = []
        if filters.get('city'):
            filters_list.append(lambda x: x.get('location', {}).get('city') == filters['city'])
        if filters.get('country'):
            filters_list.append(lambda x: x.get('location', {}).get('country') == filters['country'])
        if filters.get('price'):
            filters_list.append(lambda x: filters['price'][0] <= x.get('price') <= filters['price'][1])
        return self.__find(self.data, filters_list)

    @staticmethod
    def __find(data: Iterable, filter_funcs: Iterable[Callable]):
        res = []
        for item in data:
            for filter in filter_funcs:
                if not filter(item):
                    break
            else:
                res.append(item)
        return res
