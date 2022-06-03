from action import AbstractAction, FindHotelAction, FindTrainTicketAction, FindPlaneTicketAction, BuyHotelAction, \
    BuyTrainTicketAction, BuyPlaneTicketAction, GetPurchasesAction, AddHotelToTourAction, AddTrainTicketToTourAction, \
    AddPlaneTicketToTourAction, GetPurchasesPriceAction, BuyTourAction, GetCitiesWithHotelAction, \
    GetTrainDepartureCitiesAction, GetTrainArrivalCitiesAction, GetPlaneDepartureCitiesAction, \
    GetPlaneArrivalCitiesAction, GetTrainArrivalCitiesByDepartureAction, GetPlaneArrivalCitiesByDepartureAction
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
            'find_purchases': (GetPurchasesAction, (self.search_manager, self.purchase_manager)),
            'get_purchases_price': (GetPurchasesPriceAction, (self.purchase_manager,)),
            'add_hotel_to_tour': (AddHotelToTourAction, (self.search_manager, self.tour_manager)),
            'add_train_ticket_to_tour': (AddTrainTicketToTourAction, (self.search_manager, self.tour_manager)),
            'add_plane_ticket_to_tour': (AddPlaneTicketToTourAction, (self.search_manager, self.tour_manager)),
            'buy_tour': (BuyTourAction, (self.purchase_manager, self.tour_manager)),
            'get_cities_with_hotel': (GetCitiesWithHotelAction, (self.search_manager,)),
            'get_train_departure_cities': (GetTrainDepartureCitiesAction, (self.search_manager,)),
            'get_train_arrival_cities': (GetTrainArrivalCitiesAction, (self.search_manager,)),
            'get_train_arrival_by_departure_cities': (GetTrainArrivalCitiesByDepartureAction, (self.search_manager,)),
            'get_plane_departure_cities': (GetPlaneDepartureCitiesAction, (self.search_manager,)),
            'get_plane_arrival_cities': (GetPlaneArrivalCitiesAction, (self.search_manager,)),
            'get_plane_arrival_by_departure_cities': (GetPlaneArrivalCitiesByDepartureAction, (self.search_manager,))
        }

    def handle(self, request: Request) -> Response:
        if self.map.get(request.action):
            action, managers = self.map[request.action]
            return action(request, managers).execute()
