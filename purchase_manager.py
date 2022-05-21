from database import DB
from client import *
from purchased_ticket import *


class PurchaseManager:
    def __init__(self, data_base: DB):
        self.data_base = data_base

    @staticmethod
    def buy_hotel(client: Client, purchased_hotel: PurchasedHotel):
        DB.add_purchased_hotel_to_client(client, purchased_hotel)

    @staticmethod
    def buy_plane_ticket(client: Client, purchased_plane_ticket: PurchasedPlaneTicket):
        DB.add_purchased_plane_ticket_to_client(client, purchased_plane_ticket)

    @staticmethod
    def buy_train_ticket(client: Client, purchased_train_ticket: PurchasedTrainTicket):
        DB.add_purchased_train_ticket_to_client(client, purchased_train_ticket)

    @staticmethod
    def buy_tour(client: Client, tour: Tour):
        DB.add_tour_to_client(client, tour)
