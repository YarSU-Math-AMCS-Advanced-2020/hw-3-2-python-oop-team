from filters import HotelFilters, TicketFilters
from location import Location
from purchased_hotel import PurchasedHotel
from request import Request
import front_controller as fc
from abc import ABC, abstractmethod
from client import Client
from hotel import Hotel


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
        hotel_dict = self.front_controller.search_manager.find_hotels(HotelFilters({'id': self.args.get('id')}))
        hotel = Hotel(hotel_dict['id'], hotel_dict['title'].title, hotel_dict['price'].price,
                      Location(hotel_dict['location']['street'], hotel_dict['location']['city'],
                               hotel_dict['location']['district'], hotel_dict['location']['country']))
        purchased_hotel = PurchasedHotel(hotel, self.args.get('check_in'), self.args.get('check_out'),
                                         self.args.get('people_count'))
        self.front_controller.purchase_manager.buy_hotel(client, purchased_hotel)
