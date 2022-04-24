class Address:
    def __init__(self, country: str, region: str, city: str, street: str, building: str, apartment: int):
        self.country = country
        self.region = region
        self.city = city
        self.street = street
        self.building = building
        self.apartments = apartment

    def get_location(self):
        return f'{self.country}, {self.region}, {self.city}, {self.street}, {self.building}, {self.apartments}'
