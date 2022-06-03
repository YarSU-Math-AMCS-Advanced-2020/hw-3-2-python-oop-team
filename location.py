class Location:
    def __init__(self, street: str, district: str, city: str, country: str):
        self.street = street
        self.district = district
        self.city = city
        self.country = country

    def print_location(self):
        if self.district:
            return f'{self.country}, {self.city}, {self.district}, {self.street}'
        else:
            return f'{self.country}, {self.city}, {self.street}'
