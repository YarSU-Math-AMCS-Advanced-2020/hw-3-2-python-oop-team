from database import DB
from hotel import Hotel
from location import Location
from filters import *

if __name__ == '__main__':
    ticket_filters = TicketFilters({'to': 'Вильнюс'})  # 'from': 'Берлин'})
    db = DB('modified_train_tickets.json')
    a = db.find_tickets(ticket_filters)
    print(a)
    # hotel_filters = HotelFilters({})#{'city': 'Vilnius', 'price': (123, 4123)})
    # db = DB('modified_hotels.json')
    # a = db.find_hotels(hotel_filters)
    # hotels = []
    # for item in a:
    #     print(item)
    # for item in a:
    #     loc = Location(item['location']['street'], item['location']['district'], item['location']['city'],
    #                    item['location']['country'])
    #     hotel = Hotel(item['title'], item['price'], loc)
    #     hotels.append(hotel)
    # for hotels in hotels:
    #     hotels.print_hotel_info()
