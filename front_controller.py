from action import AbstractAction, FindHotelAction, FindTrainTicketAction, FindPlaneTicketAction, BuyHotelAction, \
    BuyTrainTicketAction, BuyPlaneTicketAction, FindPurchasesAction, AddHotelToTourAction, AddTrainTicketToTourAction, \
    AddPlaneTicketToTourAction
from request import Request
from response import Response

from purchase_manager import PurchaseManager
from search_manager import SearchManager
from tour_manager import TourManager

from typing import Dict, Type, Tuple


class FrontController:
    def __init__(self):
        self.search_manager = SearchManager()
        self.purchase_manager = PurchaseManager()
        self.tour_manager = TourManager()
        self.map: Dict[str, Tuple[Type[AbstractAction], tuple]] = {
            'find_hotels': (FindHotelAction, (self.search_manager,)),
            'find_train_tickets': (FindTrainTicketAction, (self.search_manager,)),
            'find_plane_tickets': (FindPlaneTicketAction, (self.search_manager,)),
            'buy_hotel': (BuyHotelAction, (self.search_manager, self.purchase_manager)),
            'buy_train_ticket': (BuyTrainTicketAction, (self.search_manager, self.purchase_manager)),
            'buy_plane_ticket': (BuyPlaneTicketAction, (self.search_manager, self.purchase_manager)),
            'find_purchases': (FindPurchasesAction, (self.purchase_manager,)),
            'add_hotel_to_tour': (AddHotelToTourAction, (self.search_manager, self.tour_manager)),
            'add_train_ticket_to_tour': (AddTrainTicketToTourAction, (self.search_manager, self.tour_manager)),
            'add_plane_ticket_to_tour': (AddPlaneTicketToTourAction, (self.search_manager, self.tour_manager))}

    def handle(self, request: Request) -> Response:
        if self.map.get(request.action):
            action, managers = self.map[request.action]
            return action(request, managers).execute()
