from ticket import PlaneTicket
from ticket import TrainTicket
from ticket import BusTicket
from location import Location
from decimal import Decimal
import datetime


class PurchasedPlainTicket(PlaneTicket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, place: int):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.place = place

    def get_place(self):
        return self.place


class PurchasedTrainTicket(TrainTicket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, place: int, car: int):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.place = place
        self.car = car

    def get_place(self):
        return self.place

    def get_car(self):
        return self.car


class PurchasedBusTicket(BusTicket):
    def __init__(self, from_location: Location, to_location: Location,
                 departure_date: datetime, arrival_date: datetime,
                 price: Decimal, place: int, car: int):
        super().__init__(from_location, to_location, departure_date,
                         arrival_date, price)
        self.place = place

    def get_place(self):
        return self.place
