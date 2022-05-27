from hotel import Hotel
from location import Location
from decimal import Decimal
import datetime


class PurchasedHotel(Hotel):
    def __init__(self, hotel: Hotel, check_in: str, check_out: str,
                 people_count: int):
        super().__init__(hotel.get_purchase_id(), hotel.get_title(),
                         hotel.get_price(), hotel.get_location())
        self.check_in = check_in
        self.check_out = check_out
        self.people_count = people_count

    def set_check_in(self, check_in: datetime):
        self.check_in = check_in

    def set_check_out(self, check_out: datetime):
        self.check_out = check_out

    def set_people_count(self, people_count: int):
        self.people_count = people_count

    def get_check_in(self):
        return self.check_in

    def get_check_out(self):
        return self.check_out

    def get_people_count(self):
        return self.people_count

    def count_price(self):
        return self.price * (self.check_in.days() - self.check_out.days()) * self.people_count
