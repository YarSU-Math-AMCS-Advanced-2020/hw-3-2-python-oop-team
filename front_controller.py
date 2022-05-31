from request import Request
from command import *
from typing import Dict, Type

from purchase_manager import PurchaseManager
from search_manager import SearchManager
from tour_manager import TourManager


class FrontController:
    def __init__(self):
        self.map: Dict[str, Type[AbstractCommand]] = {'find_hotels': FindHotelCommand,
                                                      'find_train_tickets': FindTrainTicketCommand,
                                                      'find_plane_tickets': FindPlaneTicketCommand,
                                                      'buy_hotel': BuyHotelCommand,
                                                      'buy_plane_ticket': BuyPlaneCommand,
                                                      'buy_train_ticket': BuyTrainCommand,
                                                      'find_purchases': FindPurchasesCommand,
                                                      'add_hotel_to_tour': AddHotelToTourCommand}
        self.search_manager = SearchManager()
        self.purchase_manager = PurchaseManager()
        self.tour_manager = TourManager()

    def handle(self, request: Request) -> list | dict | None:
        if self.map.get(request.command):
            return self.map[request.command](request, self).execute()
