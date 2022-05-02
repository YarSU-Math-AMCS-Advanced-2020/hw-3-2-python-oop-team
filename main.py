from database import DB
from hotel import Hotel
from location import Location

if __name__ == '__main__':
    filters = {'city': 'Vilnius', 'price': (123, 4123)}
    db = DB('modified_hotels.json')
    a = db.find_hotels(filters)
    hotels = []
    #print(a)
    for item in a:
        loc = Location(item['location']['street'], item['location']['district'], item['location']['city'],
                       item['location']['country'])
        hotel = Hotel(item['title'], item['price'], loc)
        hotels.append(hotel)
    for hotels in hotels:
        hotels.print_hotel_info()
