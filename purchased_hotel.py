from hotel import Hotel
import datetime


class PurchasedHotel(Hotel):
    def __init__(self, hotel: Hotel,
                 check_in: datetime, check_out: datetime, people_count: int):
        price = hotel.price * (check_in.days() - check_out.days()) * people_count
        super().__init__(price)
        self.hotel = hotel
        self.check_in = check_in
        self.check_out = check_out
        self.people_count = people_count

    def set_hotel(self, hotel: Hotel):
        self.hotel = hotel

    def set_check_in(self, check_in: datetime):
        self.check_in = check_in

    def set_check_out(self, check_out: datetime):
        self.check_out = check_out

    def set_people_count(self, people_count: int):
        self.people_count = people_count

    def get_hotel(self):
        return self.hotel

    def get_check_in(self):
        return self.check_in

    def get_check_out(self):
        return self.check_out

    def get_people_count(self):
        return self.people_count
