from manager import Manager
from purchase import Purchase
from tour import Tour


class TourManager(Manager):
    def __init__(self):
        super().__init__()

    def add_purchase_to_tour(self, tour: Tour, purchase: Purchase):
        if not purchase.is_tour():
            self.data_base.add_purchase_to_tour(tour, purchase)

    def find_tour(self, tour: Tour):
        return self.data_base.find_tour(tour)
