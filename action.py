from filters import HotelFilters, TicketFilters
from location import Location
from manager import Manager
from purchased_hotel import PurchasedHotel
from purchased_ticket import PurchasedPlaneTicket, PurchasedTrainTicket
from request import Request
from abc import ABC, abstractmethod
from client import Client
from hotel import Hotel
from ticket import Ticket
from tour import Tour
from response import Response

from typing import Tuple
from decimal import Decimal


class AbstractAction(ABC):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        self.action = request.action
        client_id = request.args.get('client_id')
        if client_id:
            self.client = Client(client_id)
        else:
            self.client = None
        self.args = request.args
        self.managers = managers

    @abstractmethod
    def execute(self):
        pass


class FindHotelAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]

    def execute(self) -> Response:
        return Response(Response.Type.LIST, self.search_manager.find_hotels(HotelFilters(self.args)))


class FindTrainTicketAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]

    def execute(self) -> Response:
        return Response(Response.Type.LIST, self.search_manager.find_train_tickets(TicketFilters(self.args)))


class FindPlaneTicketAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]

    def execute(self) -> Response:
        return Response(Response.Type.LIST, self.search_manager.find_plane_tickets(TicketFilters(self.args)))


class BuyHotelAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]
        self.purchase_manager = managers[1]

    def execute(self):
        if not all(
                (self.args.get('client_id'), self.args.get('id'), self.args.get('check_in'), self.args.get('check_out'),
                 self.args.get('people_count'))):
            return Response(Response.Type.BOOL, False)
        client = Client(self.args['client_id'])
        hotel_dict = self.search_manager.find_hotels(HotelFilters({'id': self.args['id']}))[0]
        hotel = Hotel(hotel_dict['id'], hotel_dict['title'], hotel_dict['price'],
                      Location(hotel_dict['location']['street'], hotel_dict['location']['district'],
                               hotel_dict['location']['city'], hotel_dict['location']['country']))
        purchased_hotel = PurchasedHotel(hotel, self.args['check_in'], self.args['check_out'],
                                         self.args['people_count'])
        self.purchase_manager.buy_hotel(client, purchased_hotel)
        return Response(Response.Type.BOOL, True)


class BuyTrainTicketAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]
        self.purchase_manager = managers[1]

    def execute(self):
        if not all((self.args.get('client_id'), self.args.get('id'), self.args.get('seat'),
                    self.args.get('carriage'))):
            return Response(Response.Type.BOOL, False)
        client = Client(self.args['client_id'])
        train_dict = self.search_manager.find_train_tickets(TicketFilters({'id': self.args['id']}))[0]
        train_ticket = Ticket(train_dict['id'], train_dict['departure_time'], train_dict['arrival_time'],
                              train_dict['departure_date'], train_dict['arrival_date'], train_dict['duration'],
                              train_dict['price'], train_dict['from'], train_dict['to'])
        purchased_train_ticket = PurchasedTrainTicket(train_ticket, self.args['seat'], self.args['carriage'])
        self.purchase_manager.buy_train_ticket(client, purchased_train_ticket)
        return Response(Response.Type.BOOL, True)


class BuyPlaneTicketAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]
        self.purchase_manager = managers[1]

    def execute(self):
        if not all((self.args.get('client_id'), self.args.get('id'), self.args.get('seat'))):
            return Response(Response.Type.BOOL, False)
        client = Client(self.args['client_id'])
        plane_dict = self.search_manager.find_plane_tickets(TicketFilters({'id': self.args['id']}))[0]
        plane_ticket = Ticket(plane_dict['id'], plane_dict['departure_time'], plane_dict['arrival_time'],
                              plane_dict['departure_date'], plane_dict['arrival_date'], plane_dict['duration'],
                              plane_dict['price'], plane_dict['from'], plane_dict['to'])
        purchased_plane_ticket = PurchasedPlaneTicket(plane_ticket, self.args['seat'])
        self.purchase_manager.buy_plane_ticket(client, purchased_plane_ticket)
        return Response(Response.Type.BOOL, True)


class FindPurchasesAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]
        self.purchase_manager = managers[1]

    def execute(self):
        if not self.args.get('client_id'):
            return Response(Response.Type.BOOL, False)
        client = Client(self.args['client_id'])
        return Response(Response.Type.LIST, self.purchase_manager.find_purchases(client))


class GetPurchasesPriceAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.purchase_manager = managers[0]

    def execute(self):
        if not self.args.get('client_id'):
            return Response(Response.Type.BOOL, False)
        client = Client(self.args['client_id'])
        purchases = self.purchase_manager.find_purchases(client)
        price = Decimal(0)
        for purchase in purchases:
            price += purchase.count_price()
        return Response(Response.Type.DECIMAL, price)


class AddHotelToTourAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]
        self.tour_manager = managers[1]

    def execute(self):
        if not all(
                (self.args.get('tour_id'), self.args.get('id'), self.args.get('check_in'), self.args.get('check_out'),
                 self.args.get('people_count'))):
            return Response(Response.Type.BOOL, False)
        tour = Tour(self.args['tour_id'])
        hotel_dict = self.search_manager.find_hotels(HotelFilters({'id': self.args['id']}))[0]
        hotel = Hotel(hotel_dict['id'], hotel_dict['title'], hotel_dict['price'],
                      Location(hotel_dict['location']['street'], hotel_dict['location']['city'],
                               hotel_dict['location']['district'], hotel_dict['location']['country']))
        purchased_hotel = PurchasedHotel(hotel, self.args['check_in'], self.args['check_out'],
                                         self.args['people_count'])
        self.tour_manager.add_purchase_to_tour(tour, purchased_hotel)
        return Response(Response.Type.BOOL, True)


class AddTrainTicketToTourAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]
        self.tour_manager = managers[1]

    def execute(self):
        if not all((self.args.get('tour_id'), self.args.get('id'), self.args.get('seat'),
                    self.args.get('carriage'))):
            return Response(Response.Type.BOOL, False)
        tour = Tour(self.args['tour_id'])
        train_dict = self.search_manager.find_train_tickets(TicketFilters({'id': self.args.get('id')}))[0]
        train_ticket = Ticket(train_dict['id'], train_dict['departure_time'], train_dict['arrival_time'],
                              train_dict['departure_date'], train_dict['arrival_date'], train_dict['duration'],
                              train_dict['price'], train_dict['from'], train_dict['to'])
        purchased_train_ticket = PurchasedTrainTicket(train_ticket, self.args['seat'], self.args['carriage'])
        self.tour_manager.add_purchase_to_tour(tour, purchased_train_ticket)
        return Response(Response.Type.BOOL, True)


class AddPlaneTicketToTourAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.search_manager = managers[0]
        self.tour_manager = managers[1]

    def execute(self):
        if not all((self.args.get('tour_id'), self.args.get('id'), self.args.get('seat'))):
            return Response(Response.Type.BOOL, False)
        tour = Tour(self.args['tour_id'])
        plane_dict = self.search_manager.find_plane_tickets(TicketFilters({'id': self.args['id']}))[0]
        plane_ticket = Ticket(plane_dict['id'], plane_dict['departure_time'], plane_dict['arrival_time'],
                              plane_dict['departure_date'], plane_dict['arrival_date'], plane_dict['duration'],
                              plane_dict['price'], plane_dict['from'], plane_dict['to'])
        purchased_plane_ticket = PurchasedPlaneTicket(plane_ticket, self.args['seat'])
        self.tour_manager.add_purchase_to_tour(tour, purchased_plane_ticket)
        return Response(Response.Type.BOOL, True)


class BuyTourAction(AbstractAction):
    def __init__(self, request: Request, managers: Tuple[Manager]):
        super().__init__(request, managers)
        self.purchase_manager = managers[0]
        self.tour_manager = managers[1]

    def execute(self):
        if not all((self.args.get('tour_id'), self.args.get('client_id'))):
            return Response(Response.Type.BOOL, False)
        client = Client(self.args['client_id'])
        tour = Tour(self.args['tour_id'])
        if not self.tour_manager.find_tour(tour):
            return Response(Response.Type.BOOL, False)
        self.purchase_manager.buy_tour(client, tour)
        return Response(Response.Type.BOOL, True)
