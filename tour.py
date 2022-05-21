from client import Client
from decimal import Decimal
from hotel import Hotel
from ticket import Ticket, PlainTicket, TrainTicket, BusTicket
from purchase import Purchase
import datetime


class Tour(Purchase):
    def __init__(self, purchase_list: list[Purchase]):
        self.purchase_list = purchase_list

    def get_purchase_list(self):
        purchase_list_copy = self.purchase_list
        return purchase_list_copy

    def count_price(self):
        price_sum = 0.0
        for i in self.purchase_list:
            price_sum += i
        return price_sum


# TODO add super().__init__
