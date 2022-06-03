from ticket import Ticket


class PurchasedPlaneTicket(Ticket):
    def __init__(self, ticket: Ticket, seat: int):
        super().__init__(ticket.purchase_id, ticket.departure_time, ticket.arrival_time,
                         ticket.departure_date, ticket.arrival_date, ticket.duration,
                         ticket.price, ticket.from_location, ticket.to_location)
        self.seat = seat

    def _seat(self):
        return self.seat

    def set_seat(self, seat: int):
        self.seat = seat

    def info(self):
        return f'{super().info()}Seat: {self.seat}\n'


class PurchasedTrainTicket(Ticket):
    def __init__(self, ticket: Ticket, seat: int, carriage: int):
        super().__init__(ticket.purchase_id, ticket.departure_time, ticket.arrival_time,
                         ticket.departure_date, ticket.arrival_date, ticket.duration,
                         ticket.price, ticket.from_location, ticket.to_location)
        self.seat = seat
        self.carriage = carriage

    def info(self):
        return f'{super().info()}Seat: {self.seat}\nCarriage: {self.carriage}\n'


class PurchasedBusTicket(Ticket):
    def __init__(self, ticket: Ticket, seat: int, bus_number: str):
        super().__init__(ticket.purchase_id, ticket.departure_time, ticket.arrival_time,
                         ticket.departure_date, ticket.arrival_date, ticket.duration,
                         ticket.price, ticket.from_location, ticket.to_location)
        self.seat = seat
        self.bus_number = bus_number

    def info(self):
        return f'{super().info()}Seat: {self.seat}\nBus number: {self.bus_number}\n'
