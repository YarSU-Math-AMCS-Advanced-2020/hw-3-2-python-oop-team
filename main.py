from database import DB
from hotel import Hotel
from location import Location
from filters import *
from search_manager import SearchManager

if __name__ == '__main__':
    ticket_filters = TicketFilters({'to': 'Москва'})  # 'from': 'Берлин'})
    db = DB()
    search_manager = SearchManager(db)
    # a = db.find_plane_tickets(ticket_filters)
    # for item in a:
    #     print(item)
    #print(a)
    hotel_filters = HotelFilters({'city': 'Kyiv', 'price': (123, 4123)})
    a = search_manager.find_hotels(hotel_filters)
    # hotels = []
    for item in a:
        print(item)
    # for item in a:
    #     loc = Location(item['location']['street'], item['location']['district'], item['location']['city'],
    #                    item['location']['country'])
    #     hotel = Hotel(item['title'], item['price'], loc)
    #     hotels.append(hotel)
    # for hotels in hotels:
    #     hotels.print_hotel_info()
