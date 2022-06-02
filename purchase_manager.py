from manager import Manager
from client import Client
from purchased_ticket import PurchasedPlaneTicket, PurchasedTrainTicket
from purchased_hotel import PurchasedHotel
from tour import Tour


class PurchaseManager(Manager):
    def __init__(self):
        super().__init__()

    def buy_hotel(self, client: Client, purchased_hotel: PurchasedHotel):
        self.data_base.add_purchase(client, purchased_hotel)

    def buy_plane_ticket(self, client: Client, purchased_plane_ticket: PurchasedPlaneTicket):
        self.data_base.add_purchase(client, purchased_plane_ticket)

    def buy_train_ticket(self, client: Client, purchased_train_ticket: PurchasedTrainTicket):
        self.data_base.add_purchase(client, purchased_train_ticket)

    def buy_tour(self, client: Client, tour: Tour):
        self.data_base.add_purchase(client, tour)

    def find_purchases(self, client: Client):
        return self.data_base.find_purchases(client)
