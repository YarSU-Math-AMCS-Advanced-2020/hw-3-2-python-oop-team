from database import DB
from client import *
from purchased_ticket import *
from tour import *


class TourManager:
    def __init__(self):
        self.data_base = DB()

    @staticmethod
    def add_purchased_hotel_to_tour(tour: Tour, purchased_hotel: PurchasedHotel):
        tour.add_purchase(purchased_hotel)

    @staticmethod
    def add_purchased_plane_ticket_to_tour(tour: Tour, purchased_plane_ticket: PurchasedPlaneTicket):
        tour.add_purchase(purchased_plane_ticket)

    @staticmethod
    def add_purchased_train_ticket_to_tour(tour: Tour, purchased_train_ticket: PurchasedTrainTicket):
        tour.add_purchase(purchased_train_ticket)

    # Если нужно воспользоваться общей функцией (замена трём предыдущим)
    def add_purchase_to_tour(self, tour: Tour, purchase: Purchase):
        addable = [PurchasedHotel, PurchasedPlaneTicket, PurchasedTrainTicket]
        if purchase in addable:
            self.data_base.add_purchase_to_tour(tour, purchase)

