from typing import List
from purchased_hotel import PurchasedHotel
from purchased_ticket import PurchasedTrainTicket, PurchasedPlaneTicket
from tour import Tour


class Client:
    def __init__(self, client_id: str):
        self.client_id = client_id
        self.first_name = 'Unknown'
        self.last_name = 'Shadow'
        self.birthdate = '1.1.1970'
        self.mail = 'noonecares@hmail.com'
        self.phone_number = '+79000000000'
        self.password = 'qwerty123'

    def registration(self, first_name: str, last_name: str, birthdate: str, mail: str, phone_number: str,
                     password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.mail = mail
        self.phone_number = phone_number
        self.password = password

    # Getters
    def get_client_id(self):
        return self.client_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birthdate(self):
        return self.birthdate

    def get_mail(self):
        return self.mail

    def get_phone_number(self):
        return self.phone_number

    def get_password(self):
        return self.password

    # Setters
    def set_client_id(self, client_id: str):
        self.client_id = client_id

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def set_last_name(self, last_name: str):
        self.last_name = last_name

    def set_birthdate(self, birthdate: str):
        self.birthdate = birthdate

    def set_mail(self, mail: str):
        self.mail = mail

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number

    def set_password(self, password: str):
        self.password = password
