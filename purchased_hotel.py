from hotel import Hotel


class PurchasedHotel(Hotel):
    def __init__(self, hotel: Hotel, check_in: str, check_out: str,
                 people_count: int):
        super().__init__(hotel.purchase_id, hotel.title,
                         hotel.price, hotel.location)
        self.check_in = check_in
        self.check_out = check_out
        self.people_count = people_count

    def count_price(self):
        return self.price * self.people_count

    def info(self):
        return f'{super().info()}Check-in: {self.check_in}\nCheck-out: {self.check_out}\n' \
               f'People count: {self.people_count}\n'
