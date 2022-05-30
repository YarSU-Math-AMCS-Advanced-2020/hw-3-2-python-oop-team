from filters import HotelFilters, TicketFilters
from location import Location
from purchased_hotel import PurchasedHotel
from purchased_ticket import PurchasedPlaneTicket, PurchasedTrainTicket
from request import Request
import front_controller as fc
from abc import ABC, abstractmethod
from client import Client
from hotel import Hotel
from ticket import Ticket


class AbstractCommand(ABC):
    def __init__(self, request: Request, front_controller):
        self.command = request.command
        client_id = request.args.get('client_id')
        if client_id:
            self.client = Client(client_id)
        else:
            self.client = None
        self.args = request.args
        self.front_controller = front_controller

    @abstractmethod
    def execute(self):
        pass


class FindHotelCommand(AbstractCommand):
    def __init__(self, request: Request, front_controller):
        super().__init__(request, front_controller)

    def execute(self) -> list | dict | None:
        return self.front_controller.search_manager.find_hotels(HotelFilters(self.args))


class FindTrainTicketCommand(AbstractCommand):
    def __init__(self, request: Request, front_controller):
        super().__init__(request, front_controller)

    def execute(self) -> list | dict | None:
        return self.front_controller.search_manager.find_train_tickets(TicketFilters(self.args))


class FindPlaneTicketCommand(AbstractCommand):
    def __init__(self, request: Request, front_controller):
        super().__init__(request, front_controller)

    def execute(self) -> list | dict | None:
        return self.front_controller.search_manager.find_plane_tickets(TicketFilters(self.args))


class BuyHotelCommand(AbstractCommand):
    def __init__(self, request: Request, front_controller):
        super().__init__(request, front_controller)

    def execute(self):
        client = Client(self.args.get('client_id'))
        hotel_dict = self.front_controller.search_manager.find_hotels(HotelFilters({'id': self.args.get('id')}))[0]
        hotel = Hotel(hotel_dict['id'], hotel_dict['title'], hotel_dict['price'],
                      Location(hotel_dict['location']['street'], hotel_dict['location']['city'],
                               hotel_dict['location']['district'], hotel_dict['location']['country']))
        purchased_hotel = PurchasedHotel(hotel, self.args.get('check_in'), self.args.get('check_out'),
                                         self.args.get('people_count'))
        self.front_controller.purchase_manager.buy_hotel(client, purchased_hotel)


class BuyTrainCommand(AbstractCommand):
    def __init__(self, request: Request, front_controller):
        super().__init__(request, front_controller)

    def execute(self):
        client = Client(self.args.get('client_id'))
        train_dict = \
            self.front_controller.search_manager.find_train_tickets(TicketFilters({'id': self.args.get('id')}))[0]
        train_ticket = Ticket(train_dict['id'], train_dict['departure_time'], train_dict['arrival_time'],
                              train_dict['departure_date'], train_dict['arrival_date'], train_dict['duration'],
                              train_dict['price'], train_dict['from'], train_dict['to'])
        purchased_train_ticket = PurchasedTrainTicket(train_ticket, self.args.get('seat'), self.args.get('carriage'))
        self.front_controller.purchase_manager.buy_train_ticket(client, purchased_train_ticket)


class BuyPlaneCommand(AbstractCommand):
    def __init__(self, request: Request, front_controller):
        super().__init__(request, front_controller)

    def execute(self):
        client = Client(self.args.get('client_id'))
        plane_dict = \
            self.front_controller.search_manager.find_plane_tickets(TicketFilters({'id': self.args.get('id')}))[0]
        plane_ticket = Ticket(plane_dict['id'], plane_dict['departure_time'], plane_dict['arrival_time'],
                              plane_dict['departure_date'], plane_dict['arrival_date'], plane_dict['duration'],
                              plane_dict['price'], plane_dict['from'], plane_dict['to'])
        purchased_plane_ticket = PurchasedPlaneTicket(plane_ticket, self.args.get('seat'))
        self.front_controller.purchase_manager.buy_plane_ticket(client, purchased_plane_ticket)


class FindPurchasesCommand(AbstractCommand):
    def __init__(self, request: Request, front_controller):
        super().__init__(request, front_controller)

    def execute(self):
        client = Client(self.args.get('client_id'))
        self.front_controller.purchase_manager.find_purchases(client)
