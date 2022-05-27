import request as rq
from command import AbstractCommand, FindHotelCommand, FindTrainTicketCommand, FindPlaneTicketCommand, BuyHotelCommand
from typing import Dict, Type

from purchase_manager import PurchaseManager
from search_manager import SearchManager


class FrontController:
    def __init__(self):
        self.map: Dict[str, Type[AbstractCommand]] = {'find_hotels': FindHotelCommand,
                                                      'find_train_tickets': FindTrainTicketCommand,
                                                      'find_plane_tickets': FindPlaneTicketCommand,
                                                      'buy_hotel': BuyHotelCommand}
        self.search_manager = SearchManager()
        self.purchase_manager = PurchaseManager()

    def handle(self, request: rq.Request) -> list | dict | None:
        if self.map.get(request.command):
            return self.map[request.command](request, self).execute()
