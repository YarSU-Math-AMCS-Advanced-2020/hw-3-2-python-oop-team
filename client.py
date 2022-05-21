import datetime
from purchased_hotel import *
from purchased_ticket import *
from tour import *


class Client:
    def __init__(self, client_id: str):
        self.client_id = client_id

        self.first_name = 'Unknown'
        self.last_name = 'Shadow'
        self.birthdate = datetime.date(1970, 1, 1)
        self.mail = 'noonecares@hmail.com'
        self.phone_number = '+79000000000'
        self.password = 'qwerty123'

        self.list_of_purchased_hotels: list[PurchasedHotel] = []
        self.list_of_purchased_train_tickets: list[PurchasedTrainTicket] = []
        self.list_of_purchased_plane_tickets: list[PurchasedPlaneTicket] = []
        self.list_of_tours: list[Tour] = []

    def registration(self, first_name: str, last_name: str, birthdate: datetime, mail: str, phone_number: str,
                     password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.mail = mail
        self.phone_number = phone_number
        self.password = password

    # TODO: getters, setters

    def add_purchased_hotel(self, purchased_hotel: PurchasedHotel):
        self.list_of_purchased_hotels.append(purchased_hotel)

    def add_purchased_plane_ticket(self, purchased_plane_ticket: PurchasedPlaneTicket):
        self.list_of_purchased_plane_tickets.append(purchased_plane_ticket)

    def add_purchased_train_ticket(self, purchased_train_ticket: PurchasedTrainTicket):
        self.list_of_purchased_train_tickets.append(purchased_train_ticket)
