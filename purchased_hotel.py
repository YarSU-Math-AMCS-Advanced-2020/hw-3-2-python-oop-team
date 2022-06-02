from hotel import Hotel


class PurchasedHotel(Hotel):
    def __init__(self, hotel: Hotel, check_in: str, check_out: str,
                 people_count: int):
        super().__init__(hotel.get_purchase_id(), hotel.get_title(),
                         hotel.get_price(), hotel.get_location())
        self.check_in = check_in
        self.check_out = check_out
        self.people_count = people_count

    def set_check_in(self, check_in: str):
        self.check_in = check_in

    def set_check_out(self, check_out: str):
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

    def info(self):
        return f'{super().info()}Check-in: {self.check_in}\nCheck-out: {self.check_out}\n' \
               f'People count: {self.people_count}\n'
