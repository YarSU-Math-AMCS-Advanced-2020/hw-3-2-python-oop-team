import datetime
from typing import List
from purchased_hotel import PurchasedHotel
from purchased_ticket import PurchasedTrainTicket, PurchasedPlaneTicket
from tour import Tour


class Client:
    def __init__(self, client_id: str):
        self.client_id = client_id

        self.first_name = 'Unknown'
        self.last_name = 'Shadow'
        self.birthdate = datetime.date(1970, 1, 1)
        self.mail = 'noonecares@hmail.com'
        self.phone_number = '+79000000000'
        self.password = 'qwerty123'

    def registration(self, first_name: str, last_name: str, birthdate: datetime, mail: str, phone_number: str,
                     password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.mail = mail
        self.phone_number = phone_number
        self.password = password

    # TODO: getters, setters
