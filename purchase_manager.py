from database import *
from client import *
from purchased_ticket import *


class PurchaseManager:
    def __init__(self):
        self.data_base = DB()

    def buy_hotel(self, client: Client, purchased_hotel: PurchasedHotel):
        self.data_base.add_purchase(client, purchased_hotel)

    def buy_plane_ticket(self, client: Client, purchased_plane_ticket: PurchasedPlaneTicket):
        self.data_base.add_purchase(client, purchased_plane_ticket)

    def buy_train_ticket(self, client: Client, purchased_train_ticket: PurchasedTrainTicket):
        self.data_base.add_purchase(client, purchased_train_ticket)

    def buy_tour(self, client: Client, tour: Tour):
        self.data_base.add_purchase(client, tour)
