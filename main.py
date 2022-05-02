from database import DB

if __name__ == '__main__':
    filters = {'city': 'London', 'price': (123, 4123)}
    db = DB('modified_hotels.json')
    a = db.find_hotels(filters)
    print(a)
