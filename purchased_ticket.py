from ticket import Ticket


class PurchasedPlaneTicket(Ticket):
    def __init__(self, ticket: Ticket, seat: int):
        super().__init__(ticket.get_purchase_id(), ticket.get_departure_time(), ticket.get_arrival_time(),
                         ticket.get_departure_date(), ticket.get_arrival_date(), ticket.get_duration(),
                         ticket.get_price(), ticket.get_from_location(), ticket.get_to_location())
        self.seat = seat

    def get_seat(self):
        return self.seat

    def set_seat(self, seat: int):
        self.seat = seat

    def info(self):
        return f'{super().info()}Seat: {self.seat}\n'


class PurchasedTrainTicket(Ticket):
    def __init__(self, ticket: Ticket, seat: int, carriage: int):
        super().__init__(ticket.get_purchase_id(), ticket.get_departure_time(), ticket.get_arrival_time(),
                         ticket.get_departure_date(), ticket.get_arrival_date(), ticket.get_duration(),
                         ticket.get_price(), ticket.get_from_location(), ticket.get_to_location())
        self.seat = seat
        self.carriage = carriage

    def get_seat(self):
        return self.seat

    def get_carriage(self):
        return self.carriage

    def set_seat(self, seat: int):
        self.seat = seat

    def set_carriage(self, carriage: int):
        self.carriage = carriage

    def info(self):
        return f'{super().info()}Seat: {self.seat}\nCarriage: {self.carriage}\n'


class PurchasedBusTicket(Ticket):
    def __init__(self, ticket: Ticket, seat: int, bus_number: str):
        super().__init__(ticket.get_purchase_id(), ticket.get_departure_time(), ticket.get_arrival_time(),
                         ticket.get_departure_date(), ticket.get_arrival_date(), ticket.get_duration(),
                         ticket.get_price(), ticket.get_from_location(), ticket.get_to_location())
        self.seat = seat
        self.bus_number = bus_number

    def get_seat(self):
        return self.seat

    def get_bus_number(self):
        return self.bus_number

    def set_seat(self, seat: int):
        self.seat = seat

    def set_bus_number(self, bus_number: str):
        self.bus_number = bus_number

    def info(self):
        return f'{super().info()}Seat: {self.seat}\nBus number: {self.bus_number}\n'
# TODO Добавить такие же поля, как и в Ticket
